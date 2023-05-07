o=open
class Person:
    def __init__(self,name:str,EmailClient:str,EmailHost:str):
        self.name=name
        self.email=EmailClient+'@'+EmailHost
class PKG:
    def __init__(self,root:str,pkg:str,project:str,GithubUser,repo:str,Py:Python):
        self.repo=f'https://github.com/{GithubUser}/{repo}'
        self.root=root
        self.pkg=pkg
        self.project=project
        self.PyEnv=Py
def Setting(tpkg:PKG,ver:str,Me:Person,tags:list):
    me,email=Me.name,Me.email
    root,pkg,project=tpkg.root,tpkg.pkg,tpkg.project
    PyVer=tpkg.PyEnv.ver
    y=tags[0]
    for x in tags[1:]:
        assert isinstance(x,str),'Tag must be string'
        y+=','+x
    now=pwd()
    mkdir(root)
    cd(root)
    with o('README.md')as f:
        info=f.read()
    with o('.pips')as f:
        pips=f.read()
        pips=pips.split('><')
    with o('setup.py','w')as f:
        f.write(f'''from setuptools import setup, find_packages

setup(
    name='{project}',
    version='{ver}',
    description='{info}',
    author='{me}',
    author_email='{email}',
    url='{github}',
    install_requires={pips},
    packages=find_packages(exclude=[]),
    keywords=['TPKG',{tag}],
    python_requires='{PyVer}',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)''')
    cd(now)