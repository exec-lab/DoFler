from distutils.core import setup
#import dofler

setup(
    name='DoFler',
    version='0.4.1.94',
    description='Dashboard of Fail',
    author='Steven McGrath',
    author_email='steve@chigeek.com',
    url='https://github.com/SteveMcGrath/DoFler',
    packages=[
        'dofler', 
        'dofler.api', 
        'dofler.parsers',
    ],
    entry_points={
        'console_scripts': [
            'dofler = dofler.svc:startup',
            ]
    },
    install_requires=[
        'bottle', 
        'sqlalchemy',
        'bottle-sqlalchemy',
        'paste',
        'pexpect',
        'jinja2',
        'requests',
        'psutil',
        'beautifulsoup',
        'markdown',
        'requests_futures',
    ],
    data_files=[
        ('/usr/share/dofler/static', [
            'static/jquery.min.js',
            'static/jquery.flot.min.js',
            'static/jquery.flot.time.min.js',
            'static/style.css',
        ]),
        ('/usr/share/dofler/docs', [
            'docs/introduction.md',
            'docs/walkthrough.md',
        ]),
        ('/usr/share/dofler/static/images', [
            'static/images/doc.png',
            'static/images/settings_api.png',
            'static/images/settings_login.png',
            'static/images/settings_parsers.png',
            'static/images/settings_server.png',
            'static/images/settings_services.png',
            'static/images/settings_users.png',
            'static/images/settings_webui.png',
            'static/images/ui_back.png',
            'static/images/ui_settings.png',
        ]),
        ('/usr/share/dofler/templates', [
            'templates/base.html',
            'templates/main.html',
            'templates/settings_base.html',
            'templates/settings_login.html',
            'templates/settings_logging.html',
            'templates/settings_doc_page.html',
            'templates/settings_users.html',
            'templates/settings_server.html',
            'templates/settings_api.html',
            'templates/settings_webui.html',
            'templates/settings_parsers.html',
            'templates/settings_services.html',
        ])
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
