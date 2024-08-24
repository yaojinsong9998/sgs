from sql.select import selectDaochu


def daochu():
    sql = 'SELECT *FROM usertest WHERE DATE > \'2024-04-23\' AND DATE < \'2024-05-01\' AND DAY >= 44 ORDER BY DAY DESC'
    # sql = 'SELECT * FROM `usertest` WHERE DAY >= 1 AND DATE < \'2022-07-27\' '
    re = selectDaochu(sql)
    # index = 1
    for r in re:
        id = str(r[0])
        password = str(r[1])
        # print(index)
        print(id + ',' + password)
        # index += 1

if __name__ == '__main__':
    daochu()