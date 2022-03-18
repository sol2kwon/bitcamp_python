from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):

    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        # Entity 에서 Object 로 전환
        this = self.drop_feature(this, 'SibSp','Parch','Ticket','Cabin')
        # self.kwargs_sample(name='이순신')
        '''
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''

        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id 의 타입  {type(this.id)}')
        ic(f'10. id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        ic(type(feature))
        '''
        for i in [this.train, this.test]:
            for j in feature:
                i.drop(j, axis=1, inplace=True)'''
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs)) # ic| type(feature): <class 'tuple'>
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()} # key:name, val:이순신

    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this)->object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this)->object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this