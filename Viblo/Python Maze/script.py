from __future__ import absolute_import
import sys
flag = [
    0x12166C8546F1DA8790605966DDB4D033242B5DC8E5938342CF0D5A6B6804D426311F2E3E5F9EBB2B2436CBD5F19A18CA7A054C47EF49,
    0x131E9C2B7676FC6E3583499C1376C4C1BF03764D7ABBBC7CB03604D273AA43BF21BBB484FBA7157C1809B575E83191242EE7CCE1186F,
    0x1135FEB02A9CCD8848E7EBB0F06A7F164DA1EF9D29A773D26AC6940295101435B2A05079F5D2138FD95895125B179B911335F766F728,
    0x123E1B066CFD8BB0C6DE17282D269D19D93408F7D876F0B8F0CEFAEA3C914256B68A41F26A34705C55EE99F4EA2CE1B1392F22764C3E,
    0x15C519AA97BA448F99C7DF74DB0834CAEBD57169D430EA6AF7E1799E037128719DB84D8B8E53D8BED6CA7D1BAC782F12BE92C29D402A,
    0x127031C789F043771D73E331DA83C10B39052334F88307CE5BECD2BC51DEC8D1F30EAA93B05CEA608A344F10BD29BA0CFB68CF1E1593,
    0x13A53129DD2B950960F8D39E85447F70977DAE09B020B4A293690B78CBB20A764885CB50DF1251125BEBC91F2AE95297656FDE81EFE6,
    0xF6FEEBF8CA178FF92A89E3B7CEAD86C5CA0BED4292368E5AB9AD9CD1E4FB21792932F358078AEF049F43BA068B3FFE4E0ADAA5F04EE,
    0x10D704E2FCCF82582CC35AB1D508BAC31AEA63E600CD2CCF4E34EA5BAD707A37248EB893F5568FA64FF16ACAA97070CB0CEE666AA896,
    0xBF37EB286780323630CB8387237046BB7D1EDECEE8C8F0785AB05B8198BAF949FD78BF65C42B3C4ACDE32F3E75118C788CD9E4BC692,
    0x94D01336534BB01FEC8225FAAA594628AFFF2D0951761193DFF90EC89C4CAE223DAF2EFC995F081EE1D6B4E230A7AD8F922A88F9ED7,
    0x137D82A8B71FE3E02A7B15DD35D2B289E27502DABD3D472C71A76AF9F7259C45C31AB79CD47C9BE12A33FB00325689B0A646085392F1,
    0x10D704E2FCCF82582CC35AB1D508BAC31AEA63E600CD2CCF4E34EA5BAD707A37248EB893F5568FA64FF16ACAA97070CB0CEE666AA896,
    0x156B411A7B26E99217382113F8C4261A887EDED2B0A4BF8F5294C5AE42726C946892EC95546BB5B1EB5022911D4CEE4397F82B89E220,
    0x89E96CF78AE020AE6B8BBF571B290AC05019FB812DEAC6AE9B65ED667F94FF4F52DE8FE7E4BC566604804E8F802A3C1C5A3AACC9BFB,
    0xF163C3DF11DCF50C82AFE61331FF5F160D27EE260DAB1CC7F9A857597BE09E4FEBACB7C7FF1E1A2326FFE95D7810840F127E36C9124,
    0x10D704E2FCCF82582CC35AB1D508BAC31AEA63E600CD2CCF4E34EA5BAD707A37248EB893F5568FA64FF16ACAA97070CB0CEE666AA896,
    0x123E1B066CFD8BB0C6DE17282D269D19D93408F7D876F0B8F0CEFAEA3C914256B68A41F26A34705C55EE99F4EA2CE1B1392F22764C3E,
    0x925526BA61BF0722ED73F4BC1FB3FBE3B3EA3C93F3907344076E49AFB4A1F557BE079397286F258A0E3D49F65D836FB304C26347F42,
    0x1485B24EE6A505C6CF9E06126B94A7187D4D1B5F5265806652D0156102CB0BDEB3B73DE37084F6321E06E4A028EE020A5B2888ECBC17,
    0x10D704E2FCCF82582CC35AB1D508BAC31AEA63E600CD2CCF4E34EA5BAD707A37248EB893F5568FA64FF16ACAA97070CB0CEE666AA896,
    0xE08D89C1C736FA6F88DE1C524CCF6159E5719C25179A4FC0900C93E8F2EE9F80097A5D70B9ACE3A43F70C7627F78EFEB46CEE536146,
    0x14B294CBB1D5F4B33095F03A93977F4C59F91329BF81C1730A02C7AFD4412A6346A8F0F65369647A4A64BB3EDA72CBD9A22AD39B1FC4,
    0x1485B24EE6A505C6CF9E06126B94A7187D4D1B5F5265806652D0156102CB0BDEB3B73DE37084F6321E06E4A028EE020A5B2888ECBC17,
    0x1619AAEF2203FE0BCAB0ACB0EBB561A31842B83B972B855CAC9CD83E6361F282D8A47A54C84745305061EA691B2F3CBFCE6B8FA6C36C]
b = 0

def t():
    # print ('Welcome to the s/quit game'
    # print ('You are in a mazes, c a door from 1 to 8 to continue the way'

    try:
        e = int(raw_input('Door: '))
        if e != 7 - 6:
            print ('Wrong door, QUIT')
        else:
            print ('Well done, now you can pick a number, if you c right 25 times, you will escape :D')
            for i in xrange(0, 25):
                c = int(raw_input(str(i) + ': '))
                s(i, c)

            if b == 25:
                print ('Woo hoo, you escaped!!, better make a harder maze next b')
            else:
                print ('You are trapped forever :D')
    except Exception:
        e = None
        print (e)
        print ('Something wrong :((, QUIT')
        sys.exit(1)




def s(l, _):
    global b
    for i in range(69):
        _ = m(_)

    f(_)
    if flag[l] == _:
        # print ('Great, now make the next move')
        return(1)
        b += 1
    else:
        # print ('WRONG')
        return(0)


def f(n):
    n = n >> 2
    n += 5
    if n % 2 == 0:
        return n ^ 2
    return  + 5 ^ 5


def m(_):

    _ = (_ * 69 - 78) + 84 - -69
    return x(_ ^ 3)


def x(_):
    for i in range(7):
        _ = _ ^ 7

    return _

if __name__ == ('__main__'):
    # t()

    s(0,0x61)
    for k in range(25):
        for i in range(0x20, 0x7f):
            if s(k,i) == 1:
                print(chr(i), end = '')


# flag{hoW_C4n_y0U_g3t_Out}