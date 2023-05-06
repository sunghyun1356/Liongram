from django.contrib import admin

from .models import Post, Comment




class CommnetInlines(admin.TabularInline):
    model = Comment
    extra = 5
    min_num =3
    max_num = 5
    verbose_name = '댓글 적기'

@admin.register(Post)

class PostModelAdmin(admin.ModelAdmin):
    list_display =('id','image','content','created_at','view_count','writer') #모델의 속성명을 불러온다
    list_filter = ('created_at', ) #filter로 조건
    search_fields = ('id', 'writer__username',) #id, writer로 검색 가능
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    inlines =[CommnetInlines]
    readonly_fields = ('created_at', )

    actions =['make_published']
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제'
            item.save()

#admin.site.register(Comment)


# Register your models here.
