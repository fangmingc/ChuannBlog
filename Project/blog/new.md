## 博客

### 需求


### 表设计
- 表关系图

<img src="http://chuann.cc/Project/table_relationship.png" width="700px">

- 代码

```
class User(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="密码", max_length=64)


class UserInfo(models.Model):
    """
    用户详细表
    """
    user = models.OneToOneField(verbose_name="关联用户", to="User")

    nickname = models.CharField(verbose_name="昵称", max_length=16)
    phone = models.CharField(verbose_name="用户电话号", max_length=11, unique=True)

    email = models.EmailField(verbose_name="用户邮箱", unique=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="./upload/avatar/",
                               default="/upload/avatar/default.png")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    follow = models.ManyToManyField(verbose_name="关注的人", to="UserInfo", related_name="followed")


class Blog(models.Model):
    """
    博客表
    """
    title = models.CharField(verbose_name="个人博客名", max_length=32)
    url = models.CharField(verbose_name="博客地址", max_length=64)

    theme = models.CharField(verbose_name="博客主题样式", max_length=32, default="default")
    announcement = models.CharField(verbose_name="公告", max_length=128, default="这个人很懒，什么都没留下。")

    user = models.OneToOneField(verbose_name="所属用户", to="User")


class Tag(models.Model):
    """
    标签
    """
    title = models.CharField(verbose_name="标签名", max_length=16, unique=True)
    blog = models.ForeignKey(verbose_name="所属博客", to="Blog")


class Category(models.Model):
    """
    分类
    """
    title = models.CharField(verbose_name="分类名", max_length=16)
    description = models.TextField(verbose_name="分类描述", max_length=1000, null=True)
    blog = models.ForeignKey(verbose_name="所属博客", to="Blog")

    class Meta:
        unique_together = (("title", "blog"),)


class Article(models.Model):
    """
    文章表
    """
    title = models.CharField(verbose_name="文章标题", max_length=128)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="最后更新时间", auto_now=True)
    summary = models.CharField(verbose_name="文章摘要", max_length=255, default="")
    category = models.IntegerField(verbose_name="文章类型", choices=((1, "编程语言"), (2, "软件设计"),
                                                                 (3, "前端"), (4, "数据库"), (5, "操作系统"),
                                                                 (6, "算法"), ))

    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    down_count = models.ImageField(verbose_name="踩灭数", default=0)
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    read_count = models.IntegerField(verbose_name="阅读数", default=0)
    is_essence = models.BooleanField(verbose_name="是否是精华", default=0)
    is_top = models.BooleanField(verbose_name="是否置顶", default=0)

    author = models.ForeignKey(verbose_name="作者", to="User")
    personal_category = models.ForeignKey(verbose_name="所属分类", to="Category", null=True)
    tags = models.ManyToManyField(verbose_name="标签",
                                  to="Tag",
                                  related_name="articles",
                                  through="Article2Tag",
                                  through_fields=("article", "tag"))


class ArticleDetail(models.Model):
    """
    文章详细
    """
    article = models.OneToOneField(verbose_name="一对一文章", to="Article", related_name="detail")
    content = models.TextField(verbose_name="文章内容")


class Article2Tag(models.Model):
    """
    文章和标签关系表
    """
    article = models.ForeignKey(to="Article")
    tag = models.ForeignKey(to="Tag")

    class Meta:
        unique_together = (("article", "tag"),)


class Comment(models.Model):
    """
    评论表
    """
    content = models.CharField(verbose_name="评论内容", max_length=255)
    create_time = models.DateTimeField(verbose_name="评论时间", auto_now_add=True)
    up_count = models.IntegerField(verbose_name="评论点赞数", default=0)

    user = models.ForeignKey(verbose_name="评论人", to="User")
    article = models.ForeignKey(verbose_name="所属文章", to="Article")
    father_comment = models.ForeignKey(verbose_name="父级评论", to="Comment", related_name="children_comment", null=True)


class ArticlePoll(models.Model):
    """
    文章点赞
    """
    is_positive = models.BooleanField(verbose_name="点赞or踩", default=True)
    create_time = models.DateTimeField(verbose_name="点赞时间", auto_now_add=True)
    article = models.ForeignKey(verbose_name="所属文章", to="Article")
    user = models.ForeignKey(verbose_name="点赞人", to="User")

    class Meta:
        unique_together = (("article", "user"), )


class CommentPoll(models.Model):
    """
    评论点赞
    """
    is_positive = models.BooleanField(verbose_name="点赞or踩", default=True)
    create_time = models.DateTimeField(verbose_name="点赞时间", auto_now_add=True)
    comment = models.ForeignKey(verbose_name="所属评论", to="Comment")
    user = models.ForeignKey(verbose_name="点赞人", to="User")

    class Meta:
        unique_together = (("comment", "user"), )
```






