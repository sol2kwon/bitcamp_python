# https://github.com/datasciencedojo/datasets
from titanic.views import TitanicView
from titanic.models import TitanicModel
from titanic.template import TitanicTemplate
if __name__ == '__main__':
    view = TitanicView()
    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu =='1':
         print('### 1.템플릿 ###')
         template = TitanicTemplate(fname = 'train.csv')
         template.visualize()
         template.draw_survived()
         break
        elif menu=='2':
         print('### 2.전처리 ###')
         model = TitanicModel(train_fname='train.csv',test_fname = 'test.csv')
         break