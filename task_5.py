class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Это ручка.')


class Pencil(Stationery):
    def draw(self):
        print('Это карандаш.')


class Handle(Stationery):
    def draw(self):
        print('Это маркер.')


st = Stationery('Отрисовка')
print(st.title)
st.draw()

pn = Pen('pen')
print(pn.title)
pn.draw()

ps = Pencil('pencil')
print(ps.title)
ps.draw()

hn = Handle('handle')
print(hn.title)
hn.draw()
