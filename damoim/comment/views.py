from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from post.models import Post
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from account.models import User

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['POST'])
    def create_comment(self,request):
        header = request.META['HTTP_AUTHORIZATION'][6:]
        user = User.objects.get(token = header)
        if user:
            data = JSONParser().parse(request)
            print(data['contents'],data['post_id'])
            post = Post.objects.get(id = data['post_id'])
            if post:
                Comment.objects.create(
                    writer = user.name,
                    post_id = post,
                    contents = data['contents']
                )
            return Response("생성되었습니다.",HTTP_200_OK)

        return Response("유효하지 않은 데이터.",HTTP_400_BAD_REQUEST)

comment_create = CommentViewSet.as_view({
    'get':'list',
    'post':'create_comment',
})
    
