from flask_assets import Environment, Bundle

assets = Environment()

common_css = Bundle(
    'less/main.less',
    filters=['less', 'cssmin'],
    output='gen/packed.css',
)
assets.register('common_css', common_css)
