

from snakefoot import Server, render_template, send_from_directory


class HomePageServer():

    def __init__(self):
        self.index_page = "homepage.template.html"

    def get_blog(self, req):
        blog_name = req["blog_name"]
        html = render_template(blog_name+".html")
        return {"html":html}

    def get_blog_intro_list(self, req):
        html = render_template("blog_intro.html")
        return {"html":html}


def AddRoute(app):

    def render_homepage(name):
        main_content_string = render_template(name+".html")
        html = render_template("homepage.template.html", main_content_string=main_content_string)
        return html

    @app.route("/", methods=["GET"])
    def index():
        return render_homepage("blog_intro")

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('./static/js', path)

    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('./static/css', path)

    @app.route('/image/<path:path>')
    def send_image(path):
        return send_from_directory('./static/image', path)

    @app.route("/blog/introlist")
    def get_blog_intro_list():
        return render_homepage("blog_intro")
    
    @app.route("/blog/name/<blog_name>")
    def get_blog_by_name(blog_name):
        return render_homepage(blog_name)

    blog_name_id_dict = {

    }
    @app.route("/blog/id/<blog_id>")
    def get_blog_by_id(blog_id):
        blog_name = blog_name_id_dict[blog_id]
        return render_homepage(blog_name)

    @app.route("/author")
    def get_author_info():
        return render_homepage("aaronyin-intro.html")

if __name__ == '__main__':
    s = Server(HomePageServer())
    AddRoute(s.app)
    s.bind(host="0.0.0.0", port=10091, debug=True)
    s.run()










