from django.forms import Form, CharField, Textarea


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your post here")

class CommentPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your comment here")