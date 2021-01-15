# 2.9
def start_page():

    html = """<!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" type="text/css" href="styles.css">
            <title>Document</title>
        </head>
        <body>
            <div id="container">
                <h1>Worm City!</h1>
                <a href="pick-worm.html"><button>start</button></a>
            </div>
        </body>
    </html>
    """

    f = open("start.html", "w")
    f.write(html)
    f.close()

    # def game():
    #     html = """<!DOCTYPE html>
    #     <html>
    #         <head>
    #             <meta charset="UTF-8">
    #             <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #             <link rel="stylesheet" type="text/css" href="styles.css">
    #             <title>Document</title>
    #         </head>
    #         <body>
    #             <div id="container">
    #                 <h2>Welcome to Worm City, babey!</h2>
    #                 <h4>First thing is first, what do you look like?</h4>
    #                 <div id="options">
    #                     <button onClick="color(pink)">pink</button>
    #                     <button onClick="color(yellow)">yellow</button>
    #                     <button onClick="color(purple)">purple</button>
    #                     <button onClick="color(blue)">blue</button>
    #                     <button onClick="color(green)">green</button>
    #                     <button onClick="color(orange)">orange</button>
    #                 </div>
    #             </div>
    #         </body>
    #     </html>
    #     """

    # def choose_option():
    #     answer_code = ""


start_page()
