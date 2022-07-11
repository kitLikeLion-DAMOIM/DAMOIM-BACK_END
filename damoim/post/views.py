from .models import Post
from group.models import Group
from .serializers import PostSeiralizer,PostCreateSerializer,PostListSeiralizer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK


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
        data = JSONParser().parse(request)
        print(data['title'],data['body'],data['group_id'])
        group = Group.objects.get(id = data['group_id'])
        if group:
            Post.objects.create(
                title = data['title'],
                group_id = group,
                body = data['body']
            )
            return Response("생성되었습니다.",HTTP_200_OK)
        return Response("유효하지 않은 데이터.",HTTP_400_BAD_REQUEST)


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
post_create = PostListViewSet.as_view({
    'get':'list',
    'post':'create_post',
})