from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer

# class ProductsView(APIView):
#   def get(self,request,*args,**kwargs):
#     return Response({"msg":"inside product get"})
#
# class MorningView(APIView):
#   def get(self,request,*args,**kwargs):
#     return Response({"msg":"good morning"})
#
# class EveningView(APIView):
#   def get(self,request,*args, **kwargs):
#     return Response({"msg": "good evening"})
#
#
# # class AddView(APIView):
# #   def get(self,request,*args,**kwargs):
# #     n1=int(input("Enter the no:"))
# #     n2=int(input("Enter the no:"))
# #     res=n1+n2
# #     return Response({"result":res})
#
#
# # class SubView(APIView):
# #   def get(self,request,*args,**kwargs):
# #     n1=int(input("Enter the no:"))
# #     n2=int(input("Enter the no:"))
# #     res=n1-n2
# #     return Response({"result":res})
#
# # class AddView(APIView):
# #   def post(self,request,*args,**kwargs):
# #     print(request.data.get("num1"))
# #     print(request.data.get("num2"))
# #
# #     return Response({"msg":"inside post"})
#
# class AddView(APIView):
#   def post(self,request,*args,**kwargs):
#     n1=request.data.get("num1")
#     n2=request.data.get("num2")
#     res=int(n1)+int(n2)
#     return Response({"res":res})
#
# class SubView(APIView):
#   def post(self,request,*args,**kwargs):
#     n1=request.data.get("num1")
#     n2=request.data.get("num2")
#     res=int(n1)-int(n2)
#     return Response({"result":res})

class CubeView(APIView):
  def post(self,request,*args,**kwargs):
    n=int(request.data.get("num"))
    res=n**3
    return Response({"result":res})

class NumchckView(APIView):
  def post(self,request,*args,**kwargs):
    n=int(request.data.get("num"))
    res=""
    if(n%2==0):
      res="num is even"
    else:
      res="num is odd"
    return Response(data=res)

class FactorialView(APIView):
  def post(self,request,*args,**kwargs):
    n=int(request.data.get("num"))
    res=1
    for i in range(1,(n+1)):
      res=res*i
    return Response(data=res)

class WordCountView(APIView):
  def post(self,request,*args,**kwargs):
    txt=request.data.get("text")
    words=txt.split(" ")
    wc={}
    for w in words:
      if w in wc:
        wc[w]+=1
      else:
        wc[w]=1

    return Response(data=wc)


class ProductView(APIView):

  def get(self,request,*args,**kwargs):
    qs=Books.objects.all()
    serializer=BookSerializer(qs,many=True)
    return Response(data=serializer.data)

  def post(self,request,*args,**kwargs):
    # bname=request.data.get("name")
    # bauthor=request.data.get("author")
    # bprice=request.data.get("price")
    # bpublisher=request.data.get("publisher")
    # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
    # return Response(data="created")
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
      Books.objects.create(**serializer.validated_data)
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)


class ProductDetailsView(APIView):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("id")
    Book=Books.objects.get(id=id)
    serializer=BookSerializer(Book,many=False)
    return Response(data=serializer.data)

  def  delete(self,request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    return Response(data="deleted")

  def put(self,request,*args,**kwargs):
    id=kwargs.get("id")
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
      Books.objects.filter(id=id).update(**serializer.validated_data)
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)


class ReviewsView(APIView):
  def get(self,request,*args,**kwargs):
    reviews=Reviews.objects.all()
    serializer=ReviewSerializer(reviews,many=True)
    return Response(data=serializer.data)

  def post(self,request,*args,**kwargs):
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("id")
    qs=Reviews.objects.get(id=id)
    serializer=ReviewSerializer(qs,many=False)
    return Response(data=serializer.data)

  def put(self,request,*args,**kwargs):
    id=kwargs.get("id")
    object=Reviews.objects.get(id=id)
    serializer=ReviewSerializer(instance=object,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)

  def delete(self,request,*args,**kwargs):
    id=kwargs.get("id")
    Reviews.objects.get(id=id).delete()
    return Response(data="deleted")