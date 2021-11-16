# # Import Flask class và hàm render_template để render file HTML
# from flask import Flask, render_template, request


# # Khởi tạo Flask app và kiểm tra xem nó là main script hay imported
# app = Flask(__name__)

# movies = {
#     "1": {
#         "id": 1,
#         "title": "Squid Game",
#         "year": 2021
#     },
#     "2": {
#         "id": 2,
#         "title": "My Name",
#         "year": 2020
#     }
# }


# # Chỉ định URL kích hoạt hàm homepage
# @app.route("/")
# # Hàm homepage() chạy khi đường dẫn khớp với route /
# def homepage():
#     # Render file HTML và trả về cho trình duyệt
#     # Truyền dữ liệu để render
#     return render_template("index.html", movies=movies)


# @app.route("/about")
# def about():
#     return render_template("about.html")

# # Tham số URL
# @app.route("/movies/<movie_id>")
# # Tham số trong URL sẽ được truyền cho hàm
# def detail(movie_id):
#     movie = movies.get(movie_id)
#     return render_template("movie.html", movie=movie)


# # Kiểm tra nếu là main script
# if __name__ == "__main__":
#     # Chạy Flask app
#     # Bật debug để restart server mỗi khi có thay đổi trong mã
#     app.run(debug=True)



from flask import Flask, render_template, Response, request, redirect
from flask.globals import request

app = Flask(__name__)

blogs={
    "101":{
        "id":101,
        "title":"Hanh oi",
        "content":"Hanh day !",
        "postat": "10h"

    },
    "102":{
        "id":102,
        "title":"Hanh oi",
        "content":"Hanh day !",
        "postat": "10h"

    }
}

## jinja template 
@app.route("/")
def index():
    return render_template("index.html", blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/', methods=["GET"])
def render_form():
    return render_template("new-blog.html")

@app.route("/", methods=["POST"])
def new_blog():
    # print("Nhan yeu cau post")
    print(request.form)
    title=request.form["title"]
    # postat=request.form["postat"]
    content=request.form["content"]

    blogs["len(blogs)"]={"id":103, "title":title, "content": content , "postat":"10h"}
    print("Da nhan yeu cau")
    return redirect("/", code=302)
    # return "Da nhan yeu cau"

#path param
#movies/1 movies/2 movies/id
@app.route("/blogs/<blog_id>")
def detail(blog_id):
    # movie=movies[movie_id]
    blog=blogs.get(blog_id)
    return Response(render_template("blog.html", blog=blog), status=200, mimetype="text/html")


@app.route("/blogs/edit/<idd>", methods=["GET"])
def edit_blog(idd):
    print ("Edit blog")
    blog=blogs.get(idd)
    
    return Response(render_template("edit-blog.html", blog=blog), status=200, mimetype="text/html")

@app.route("/blogs/edit/<idd>", methods=["POST"])
def update_blog(idd):
    blog=blogs.get(idd)
    blog['title']=request.form["title"]
    # postat=request.form["postat"]
    blog['content']=request.form["content"]
    

    return Response(render_template("edit-blog.html", blog=blog), status=200, mimetype="text/html")
   

@app.route("/blogs/register", methods=["GET"])
def render_register():
    return render_template("new-blog.html")

@app.route("/blogs/register", methods=["POST"])
def blog_register():
    print("Đăng kí thành công chưa ?")
    return "Dang ki thanh cong !"


if __name__=="__main__":
    app.run(debug=True)