from rest_framework.response import Response
from rest_framework import status, validators
from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from api.src.product.ProductModel import Product
from api.src.category.CategoryModel import Category
from rest_framework.views import APIView
from api.src.product.ProductSerializer import ProductSerializer
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getProduct(request):
    response = Response(status=status.HTTP_200_OK)
    data = {"status": False, "data": [], "message": ""}
    try:
        page = int(request.GET['page'])
        numberRecords = int(request.GET['numberRecords'])
        if page <= 0 or numberRecords <= 0:
            raise ValueError()

        offset = (page-1) * numberRecords
        products = Product.objects.all()[offset:numberRecords]
        dataReturn = ProductSerializer(products, many=True)
        data['status'] = True
        data['message'] = 'Success'
        data['data'] = dataReturn.data

    except (ValueError, KeyError):
        data['message'] = 'Please input valid params'
    except Product.DoesNotExist:
        data['message'] = 'Data is not existed'
    except Exception:
        data['message'] = 'Internal Error'

    response.data = data
    return response


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def getProductById(request):
    response = Response(status=status.HTTP_200_OK)
    data = {"status": False, "data": [], "message": ""}
    try:
        productId = int(request.GET['productId'])
        if productId <= 0:
            raise ValueError()

        product = Product.objects.get(product_id=productId)
        dataReturn = ProductSerializer(product)
        data['status'] = True
        data['message'] = 'Success'
        data['data'] = dataReturn.data

    except (ValueError, KeyError):
        data['message'] = 'Please input valid params'
    except Product.DoesNotExist:
        data['message'] = 'Data is not existed'
    except Exception:
        data['message'] = 'Internal Error'

    response.data = data
    return response


@api_view(['POST'])
def createProduct(request):
    response = Response(status=status.HTTP_200_OK)
    data = {"status": False, "data": [], "message": ""}
    try:
        productName = str(request.data['productName'])
        categoryId = int(request.data['categoryId'])
        category = Category.objects.get(category_id=categoryId)

        newProduct = Product()
        newProduct.product_name = productName
        newProduct.category = category
        newProduct.created_at = timezone.now()
        newProduct.updated_at = timezone.now()
        newProduct.save()
        dataReturn = ProductSerializer(newProduct)
        data['status'] = True
        data['message'] = 'Success'
        data['data'] = dataReturn.data

    except (ValueError, KeyError):
        data['message'] = 'Please input valid params'
    except Category.DoesNotExist:
        data['message'] = 'Data is not existed'
    except Exception:
        data['message'] = 'Internal Error'

    response.data = data
    return response
