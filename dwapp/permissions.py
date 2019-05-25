from rest_framework import permissions

class IsAuthOrReadOnly(permissions.BasePermission):

    
    def has_permission(self, request, view):
        return request.user.is_authenticated #권한이 있는 사람만 게시글 보이도록 설정
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # 관리자만 삭제 가능
        if request.method == 'DELETE':
            return request.user.is_superuser

        # 해당 글의 작성자일 경우에만 'PUT'요청 허용
        if request.method == 'PUT':
            return obj.author == request.user