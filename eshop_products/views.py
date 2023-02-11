import itertools
from django.shortcuts import render
from django.views.generic import ListView
from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from django.http import Http404
from eshop_products_category.models import ProductCategory
from .forms import CommentForm
from .models import Comment, Product


# Create your views here.


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('not found!')
        return Product.objects.get_products_by_category(category_name)


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']

    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})

    product = Product.objects.get_by_id(selected_product_id)

    if product is None or not product.active:
        raise Http404()

    product.visit_count += 1

    product.save()

    # comment section
    comments = product.product_comment.filter(is_active=True)
    new_comment = None
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.product_comment = product
        new_comment.save()
        comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    # end of comment section

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products = my_grouper(3, related_products)

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)

    grouped_galleries = list(my_grouper(3, galleries))

    context = {
        'title': product,
        'product': product,
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'products/product_detail.html', context)


class SearchProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)
