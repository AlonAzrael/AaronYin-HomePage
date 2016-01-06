

/* client
======================================================
*/
function replace_main_content (html) {
    var old_main_content = $(".ah-main-content")
    old_main_content.replaceWith(html)
}

function HomePageClient_C () {

    var client = snakefoot.Client()
    
    var homepage_client_obj = {

        init: function () {

        },

        get_blog_intro_list: function  () {
            client.invoke("get_blog_intro_list", {}, function (result) {
                replace_main_content(result.html)
                var blog_intro_list = $(".ah-blog-intro-title")
                
                blog_intro_list.click(function () {
                    var blog_name = $(this).attr("blog-name")
                    HOMEPAGE_CLIENT.get_blog_list(blog_name)
                })
                blog_intro_list.hover(
                function () {
                    $(this).append("☍")
                    // .addClass("ah-blog-intro-title-hover")
                }, 
                function () {
                    var x = $(this)
                    var text = x.text()
                    x.text(text.slice(0,-1))
                    // x.removeClass("ah-blog-intro-title-hover")
                })

            })
        },

        get_blog_list: function (blog_name) {
            client.invoke("get_blog", {"blog_name":blog_name}, function (result) {
                replace_main_content(result.html)
            })
        },

    }
    homepage_client_obj.init()

    return homepage_client_obj
}
HOMEPAGE_CLIENT = HomePageClient_C()


/* event binding
======================================================
*/
function event_binding () {
    $(".ah-blog-btn").click(function () {
        HOMEPAGE_CLIENT.get_blog_intro_list()
    })
}




