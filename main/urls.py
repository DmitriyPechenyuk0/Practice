from .settings import project
from home import render_home, home
from tour import render_tour, tour
# from user import render_user, user



project.add_url_rule(rule='/', view_func=render_home, methods=['GET', 'POST'])

project.add_url_rule(rule='/tour', view_func=render_tour)

project.register_blueprint(blueprint=home)

project.register_blueprint(blueprint=tour)
