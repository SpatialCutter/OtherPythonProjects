import datetime
import os.path


class Reader:
    @staticmethod
    def _ExistFile(filename: str, exception: bool =True) -> bool:
        """
        Проверяет наличие файла по указаному пути

        :param filename: имя файла для проверки
        :param exception: выдавать исключение если файл не найден
        :return: возвращает булево значение наличия файла
        """
        if not os.path.isfile(filename):
            if exception:
                raise Exception("Файл не найден!")
            else: return False
        else: return True

    @staticmethod
    def ReadValue(filename: str, convert=int, start: int =0):
        """
        Считывает одно значение из файла

        :param filename: имя файла для считывания
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param start: номер строки из которой будет считано значение
        :return: возвращает переменную введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            try:
                return convert(file.readlines()[start].strip())
            except:
                raise Exception("Данные не удалось считать или конвертировать! Проверьте данные в файле, что их хватает и что они в правильном виде!")

    @staticmethod
    def ReadText(filename: str, start: int = 0):
        """
        Считывает текст из файла

        :param filename: имя файла для считывания
        :param start: номер строки из которой будет считано значение
        :return: возвращает переменную типа str
        """
        Reader._ExistFile(filename)
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                return ''.join(file.readlines()[start:])
            except:
                raise Exception(
                    "Данные не удалось считать! Проверьте данные в файле, что их хватает и что они в правильном виде!")

    @staticmethod
    def ReadLine(filename: str, sep: str =' ', convert=int, sizeline: bool =False, start: int =0, size: int =None) -> list:
        """
        Считывает строку значений из файла

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены значения в строке
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param sizeline: наличие строки размеров, которая идёт перед строкой
        :param start: номер строки которая будет считана
        :param size: количество значений в строке, которое нужно считать (не учитывается при sizeline = True)
        :return: возвращает список переменных введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            data = file.readlines()
            answer = []
            try:
                if sizeline:
                    size = int(data[start].strip())
                    start+=1
                answer.extend(map(convert, data[start].split(sep)[:size]))
                return answer
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadSomeLines(filename: str, sep: str =' ', convert=int, start: int =0, size: int =None) -> list:
        """
        Считывает несколько строк значений разделённых пустой строкой из файла

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены значения в строке
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param start: номер строки, с которой начнётся считывание
        :param size: количество строк (учитывая пустые), которые нужно считать (не учитывается при sizeline = True)
        :return: возвращает список, содержащий списки переменных введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            answer = []
            temp = []
            try:
                for row in file.readlines()[start:]:
                    if (row.rstrip() == ""):
                        answer.append(temp.copy())
                        temp.clear()
                    else:
                        temp.extend(map(convert, row.split(sep))[:size])
                return answer
            except:
                raise Exception(
                    "Данные не удалось считать или конвертировать! "
                    "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadColumn(filename: str, convert=int, sizeline: bool =False, start: int =0, size: int =None) -> list:
        """
        Считывает столбец значений из файла

        :param filename: имя файла для считывания
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param sizeline: наличие строки размеров, которая идёт перед столбцом
        :param start: номер строки с которой начнётся считывание
        :param size: количество элементов в столбце, которые нужно считать (не учитывается при sizeline = True)
        :return: возвращает список переменных введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            answer = []
            try:
                data = file.readlines()
                if sizeline:
                    size = int(data[start])+1
                    start+=1
                for row in data[start:size]:
                    answer.append(convert(row.rstrip()))
                return answer
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadMatrix(filename: str, sep: str =' ', convert=int, sizeline: bool =False, start: int =0, size: tuple =(None, None)) -> list:
        """
        Считывает матрицу значений из файла

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены значения в строках
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param sizeline: наличие строки размеров, которая идёт перед матрицей
        :param start: номер строки с которой начнётся считывание
        :param size: количество элементов в матрице, которые нужно считать. принимается в виде (строка, столбец) (не учитывается при sizeline = True)
        :return: возвращает список строк матрицы с переменными введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            data = file.readlines()
            answer = []
            try:
                if sizeline:
                    size2 = list(map(int, data[start].split(sep=sep)))
                    size2[0] += 1
                    size = tuple(size2)
                    start += 1
                for row in data[start:size[0]]:
                    answer.append(list(map(convert, row.rstrip().split(sep)[:size[1]])))
                return answer
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadMatrixAsLine(filename: str, sep: str=' ', convert=int, sizeline: bool =False, start: int =0, size: tuple =(None, None)) -> list:
        """
        Считывает матрицу значений из файла в виде строки

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены значения в строке
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param sizeline: наличие строки размеров, которая идёт перед матрицей
        :param start: номер строки с которой начнётся считывание
        :param size: количество элементов в матрице, которые нужно считать. принимается в виде (строка, столбец) (не учитывается при sizeline = True)
        :return: возвращает список переменных введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            data = file.readlines()
            answer = []
            try:
                if sizeline:
                    size2 = list(map(int, data[start].split(sep=sep)))
                    size2[0] += 1
                    size = tuple(size2)
                    start += 1
                for row in data[start:size[0]]:
                    answer.extend(list(map(convert, row.rstrip().split(sep)[:size[1]])))
                return answer
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadSomeMatrix(filename: str, sep: str=' ', convert=int, start: int=0) -> list:
        """
        Считывает несколько матриц из файла разделённых пустой строкой

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены значения в строке
        :param convert: тип данных считываемый из файла, по умолчанию int
        :param start: номер строки с которой начнётся считывание
        :return: возвращает список с вложенными списками строк матрицы с переменными введённого типа данных
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            answer = []
            temp = []
            try:
                for row in file.readlines()[start:]:
                    if (row.rstrip() == ""):
                        answer.append(temp.copy())
                        temp.clear()
                    else:
                        temp.append([convert(i.rstrip()) for i in row.split(sep)])

                answer.append(temp.copy())
                return answer
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadDate(filename: str, sep: str ='.', region: str ='ru', start: int =0) -> datetime:
        """
        Считывает дату из файла

        :param filename: имя файла для считывания
        :param sep: разделитель, которым разделены день месяц год
        :param region: регион - порядок, в котором записана дата ('ru' - dd.mm.yyyy, 'us' - yyyy.mm.dd)
        :param start: номер строки из которой будет считана дата
        :return: возвращает дату
        """
        Reader._ExistFile(filename)
        with open(filename, 'r') as file:
            try:
                answer = file.readlines()[start].split(sep)
                if region == 'ru':
                    return datetime.date.fromisoformat('-'.join(answer[::-1]))
                elif region == 'us':
                    return datetime.date.fromisoformat('-'.join(answer))
            except:
                raise Exception("Данные не удалось считать или конвертировать! "
                                "Проверьте данные в файле, что их достаточно и что они в правильном виде!")

    @staticmethod
    def ReadBlocks(filename: str, inline: bool =True, sep: str =None, sizeline: bool =False) -> list:
        """
        Считывает несколько блоков данных из файла, аналогично методам ReadSomeLines и ReadSomeMatrix

        :param filename: имя файла для считывания
        :param inline: является ли блок данных строкой (При True работает аналогично ReadSomeLines)
        :param sep: разделитель, которым разделены значения в строке
        :param sizeline: наличие строки размеров, которая идёт перед каждым блоком данных (при True блоки должны быть разделены только строкой размеров)
        :return: возвращает список со вложенными списками
        """
        Reader._ExistFile(filename)
        file = open(filename, 'r')
        answer = []
        temp = []
        rownum = 0
        rowlen = 10
        if sizeline and rownum == 0:
            size = list(map(int, file.readline().split(sep)))
            temp.append(size)
            rowlen = size[0]
        for row in file.readlines():
            if (row.rstrip() == "" and not sizeline):
                answer.append(temp.copy())
                temp.clear()
            elif (sizeline and rownum == rowlen):
                answer.append(temp.copy())
                temp.clear()
                size = list(map(int, row.split(sep)))
                temp.append(size)
                rowlen = size[0]
                rownum=0
            else:
                if not inline:
                    if sep is None:
                        temp.append(row.rstrip())
                    else: temp.append(row.rstrip().split(sep))
                    rownum += 1
                else:
                    temp.append(list(map(str.rstrip, row.split(sep))))
                    rownum = rowlen

        answer.append(temp.copy())
        file.close()
        return answer


class Writer:
    @staticmethod
    def WriteValue(filename: str, value, append: bool =False):
        """
        Записывает одно значение в файл

        :param filename: имя файла для записи
        :param value: значение, которое нужно записать
        :param append: добавить ли значение в конец существующего файла
        :return: ничего не возвращает
        """
        with open(filename, 'a') if append else open(filename, 'w') as file:
            print(value, file=file)

    @staticmethod
    def WriteVector(filename: str, vector: list, sep: str =' ', append: bool =False):
        """
        Записывае вектор (строку или столбец) в файл

        :param filename: имя файла для записи
        :param vector: список, который нужно записать
        :param sep: разделитель, которым будут разделены элементы списка в файле (для столбца ввести "\n")
        :param append: добавить ли вектор в конец существующего файла
        :return: ничего не возвращает
        """
        with open(filename, 'a') if append else open(filename, 'w') as file:
            print(*vector, sep=sep, file=file)

    @staticmethod
    def WriteMatrix(filename: str, array: list, sep: str =' ', append: bool =False):
        """
        Записывает матрицу в файл

        :param filename: имя файла для записи
        :param array: список строк матрицы, который нужно записать
        :param sep: разделитель, которым будут разделены элементы строк матрицы в файле
        :param append: добавить ли матрицу в конец существующего файла
        :return: ничего не возвращает
        """
        Reader._ExistFile(filename)
        with open(filename, 'a') if append else open(filename, 'w') as file:
            for i in array:
                print(*i, sep=sep, file=file)
