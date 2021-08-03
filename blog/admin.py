from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'trim_content', 'author', 'date_posted')
    
    @admin.display(description='Content')
    def trim_content(self, obj):
        return self.remove_html_tags(obj.content)[0:150]

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

admin.site.register(Post, PostAdmin)
