from model.userfield import UserFieldsName


def test_add_user(app):
    app.open_home_page()
    app.user.add(UserFieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка",
                                title="title", company="comp", address="address", home="home", mobile="232323",
                                work="232344354", fax="232323", email="sd@test.com", email2="we@test.net",
                                email3="wewd@t.er", homepage="http://ya.ru", bday="23", bmonth="December",
                                byear="1987", address2="jhdufyhdh", phone2="233443", notes="dfdjdj"))
