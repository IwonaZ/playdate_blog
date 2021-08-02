from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint,current_app)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user, age=form.age.data, gender=form.gender.data)
        post.language_speaking = form.language_speaking.data
        post.language_learning = form.language_learning.data
        post.save()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')

@posts.route("/post/<post_id>")
def post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    post.update(inc__views=1)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/map")
@login_required
def post_map():
    posts = Post.objects.all()
    return render_template('map.html', posts=posts, map_key=current_app.config["GOOGLE_MAPS_API_KEY"])

@posts.route("/post/language/<language>", methods=['GET', 'POST'])
@login_required
def language_search(language):
    posts = Post.objects(language_speaking=language).order_by('-date_posted')
    return render_template('home.html', posts=posts)

@posts.route("/post/age/<age>", methods=['GET', 'POST'])
@login_required
def age_search(age):
    posts = Post.objects(age=age)
    toddlers = Post.objects.filter(age==3 or age==2 or age==1) 
    return render_template('home.html', posts=posts)

'''@posts.route("/post/age/<search_age>")
@login_required
def age_search(search_age):
    posts = Post.objects.get_or_404(title=search_age)
    print(posts.user_id)
    return render_template('home.html', posts=posts)'''

@posts.route("/post/<post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    if post.user_id != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.age = form.age.data
        post.gender = form.gender.data
        post.language_speaking = form.language_speaking.data
        post.language_learning = form.language_learning.data
        post.save()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.age.data = post.age
        form.gender.data = post.gender
        form.language_learning.data = post.language_learning
        form.language_speaking.data = post.language_speaking
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    if post.user_id != current_user:
        abort(403)
    post.delete()
    #db.session.delete(post)
    #db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))