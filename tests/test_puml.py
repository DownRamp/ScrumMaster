from actions import puml, saver
from puml import create_puml, create_full_puml
from saver import Document, update_docs

example = ["\\(\\*\\)\\ \\-\\->\\ 'User'\\ as\\ user\\", "user\\ \\-\\->\\ 'Website'\\ as\\ web\\", "user\\ \\-\\->\\ 'Sprint\\ update\\ \\(POST\\)'\\ as\\ upsprint\\", "web\\ \\-\\->\\ 'Create\\ doc\\ \\(POST\\)'\\ as\\ doc\\", "\\ \\ \\ \\ \\-\\->\\ 'API'\\ as\\ api\\", "web\\ \\-\\->\\ 'Create\\ ticket\\ \\(POST\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Update\\ doc\\ \\(POST\\)'\\ as\\ updoc\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Update\\ ticket\\ \\(POST\\)'\\ as\\ upticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Hiring\\ \\(POST\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Fetch\\ sprint\\ updates\\ \\(GET\\)'\\ as\\ sprint\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Backlog\\ \\(GET\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Fetch\\ full\\ view\\ \\(GET\\)'\\ as\\ full\\", "\\ \\ \\ \\ \\-\\->\\ 'Create\\ puml'\\ as\\ puml\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Rolodex\\ \\(GET\\)'\\ as\\ rolo\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Show\\ docs\\ \\(GET\\)'\\ as\\ show\\", '\\ \\ \\ \\ \\-\\->\\ puml\\', '\\ \\ \\ \\ \\-\\->\\ api\\', 'api\\ \\-\\->\\ \\(\\*\\)']
create_puml("example",example)

update_docs(Document("title1", "des1", "why","repo_conn","tests","devs","types","puml_txt"), 1)
update_docs(Document("title2", "des2", "why","repo_conn","tests","devs","types","puml_txt"), 3)
update_docs(Document("title3", "des3", "why","repo_conn","tests","devs","types","puml_txt"), 4)
update_docs(Document("title4", "des4", "why","repo_conn","tests","devs","types","puml_txt"), 5)

full_example = [[1,[3]],[3,[1]],[4,[3]],[5,[3]]]
create_full_puml("example_full", full_example)