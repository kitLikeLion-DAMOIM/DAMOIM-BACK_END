from itsdangerous import Serializer
from .models import Post
from .serializers import PostSeiralizer,PostCreateSerializer,PostListSeiralizer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostSeiralizer

    @action(detail=True, methods=['POST'])
    def create_post(self,request,pk):
        instance = self.get_object()
        instance.save()
        serializer =  self.get_serializer(instance)
        return Response(serializer.data)


class PostListViewSet(ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostListSeiralizer

    @action(detail=True)
    def post_list(self,request,pk):
        qs = self.queryset.filter(group_id=pk)
        serialzer = self.get_serializer(qs,many=True)
        return Response(serialzer.data)

    @action(detail=True, methods=['POST'])
    def create_post(self,request,pk):
        instance = self.get_object()
        instance.save()
        serializer =  self.get_serializer(instance)
        return Response(serializer.data)


class PostCreateViewSet(ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostCreateSerializer

post_list = PostListViewSet.as_view({
    'get':'post_list',
    'post':'create'
})

post_detail = PostViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
})
post_create = PostCreateViewSet.as_view({
    'get':'list',
    'post':'create',
})