from django.shortcuts import render
from library import models



from django.shortcuts import get_object_or_404
from rest_framework.views import APIView                # import API
from rest_framework.response import Response            # API Response like view
from rest_framework import status                       # status when API working
from . import serializers                               # import seializer
from rest_framework import pagination                   # import pagination

                                                                                # Pagination Main Class
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            
            },
            'count':self.page.paginator.count,
            'result':data
        })

                                                                                #Book API Class
class BookList(APIView):

    def get(self,request,id=None):
        if id == None:
            me              =   models.Book.objects.all()
            serializer      =   serializers.BookSerializer(me,many=True)
        else:
            me              =   models.Book.objects.get(id=id)
            serializer      =   serializers.BookSerializer(me)
        return Response(serializer.data)
        

    def post(self,request,format=None):
        serializer          =   serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id):
        me                  =   models.Book.objects.get(id=id)
        serializer          =   serializers.BookSerializer(me,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        me                  =   models.Book.objects.get(id=id)
        me.delete()
        return Response(status=status.HTTP_302_FOUND)


                                                                               #Book paginations Class
class BookPage(APIView):

    def get(self,request,id=None):
        sort        =   request.GET.get('sortBy')
        order       =   request.GET.get('orderBy')
        search      =   request.GET.get('name')
        data        =   ''

        if order    ==  'desc':
            data    =   models.Book.objects.filter(book_name__istartswith=search).order_by(sort)[::-1]
        elif order  ==  'asc':
            data    =   models.Book.objects.filter(book_name__istartswith=search).order_by(sort)
        
        serializer  =   serializers.BookSerializer(data,many=True)
        paginator   =   CustomPagination()
        paginator.page_size = request.GET.get('itemPerPage')
        result_page =   paginator.paginate_queryset(data,request)
        serializer  =   serializers.BookSerializer(result_page,many=True)

        if serializer.is_valid:
            return paginator.get_paginated_response(serializer.data)
        else:
            msg = False
            error = serializer.errors
            statuss = status.HTTP_400_BAD_REQUEST
            return Response({'success':msg, 'errors':error, 'status':statuss})


class CususerList(APIView):                                                 # Abstract User API List

    def get(self,request,id=None):

        if id  ==  None:
            me              =   models.Cususer.objects.all()
            serializer      =   serializers.CususerSerializer(me,many=True)
        else:
            me              =   models.Cususer.objects.get(id=id)
            serializer      =   serializers.CususerSerializer(me)
        return Response(serializer.data)

    
    def post(self,request,format=None):

        serializer          =   serializers.CususerSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class IssuedbookList(APIView):

    def get(self,request,id=None):

        if id  ==  None:
            me              =   models.Issuedbooks.objects.all()
            serializer      =   serializers.IssuedbooksSerializer(me,many=True)
        else:
            me              =   models.Issuedbooks.objects.get(id=id)
            serializer      =   serializers.IssuedbooksSerializer(me)
        return Response(serializer.data)


    def delete(self,request,id):

        me                  =   models.Issuedbooks.objects.get(id=id)
        me.delete()
        return Response(status=status.HTTP_302_FOUND)
    





