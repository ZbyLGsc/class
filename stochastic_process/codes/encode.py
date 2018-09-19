import binary_tree
import math
import numpy as np


class LetterProb:
    def __init__(self, let, prob):
        self.letter = let
        self.prob = prob
        self.log = -1
        self.code = -1

def huffman(lplist):
    '''
    Input: list of LetterProb without code
    Output: Tree of LetterProb with code
    '''

    '# first create a list of node'
    lpnode_list = []
    for i in range(26):
        node = binary_tree.Node(lplist[i],True)
        lpnode_list.append(node)


    '# create a tree of nodes, '
    while True:
        # find the two item with the least prob
        lp12 = []
        for i in range(2):
            min_id = -1
            min = 1000
            for i in range(len(lpnode_list)):
                if lpnode_list[i].item.prob < min:
                    min_id = i
                    min = lpnode_list[i].item.prob
            lp12.append(lpnode_list[min_id])
            lpnode_list.pop(min_id)

        '# add these two nodes to a parent node and add to list'
        node = binary_tree.Node(LetterProb(lp12[0].item.letter+lp12[1].item.letter,lp12[0].item.prob+lp12[1].item.prob),False)
        node.addChild(lp12[0], lp12[1])
        lpnode_list.append(node)

        # for i in range(len(lpnode_list)):
        #     print lpnode_list[i].item.letter, lpnode_list[i].item.prob
        # print '------------------------------------------'

        if len(lpnode_list) == 1:
            break
        
    # traverse the tree
    sort_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    binary_tree.traverse(lpnode_list[0],'',sort_list)

    for i in range(len(sort_list)):
        print sort_list[i].letter, sort_list[i].prob, sort_list[i].code 



            
def getCode(num):
    '''
    Input: number of bits n
    Output: a n bit binary code
    '''
    code = ''
    for i in range(num):
        rd = np.random.rand()
        if rd > 0.5:
            code += '1'
        else:
            code += '0'

    return code


def shannonFano(lplist):
    '''
    Input: list of LetterProb without code
    Output: list of LetterProb with code
    '''    

    'cal [log(1/pi)] for every letter'
    for i in range(len(lplist)):
        lplist[i].log = int(math.floor(math.log(1/lplist[i].prob)/math.log(2)))

    # for i in range(len(lplist)):
    #     print lplist[i].letter, lplist[i].prob, lplist[i].log 

    inte = 3
    finish = 0
    while not finish>=26:
        'genertate code with length of inte'
        used_code = []
        for i in range(len(lplist)):
            if lplist[i].log == inte:
                'generate a un-used code'
                while True:
                    cd = getCode(inte)
                    if used_code.count(cd) == 0:
                        used_code.append(cd)
                        break
                
                'add the code to letter'
                lplist[i].code = cd
                finish += 1

        inte += 1
    
    for i in range(len(lplist)):
        print lplist[i].letter, lplist[i].prob, lplist[i].log, lplist[i].code 



            




def main():
    lf = file('test file for Q.4.txt','r')
    text = lf.read().lower()

    # 'list to store the occurence of each letter'
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    occ = []
    su = 0
    for i in range(26):
        num = text.count(letter[i])
        occ.append(num)
        su = su + num
    print 'Number of letter:'
    print occ, su

    for i in range(26):
        occ[i] = float(occ[i])/float(su)
    # print occ
    lf.close()

    # letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # occ = [0.0793437886917045, 0.016611638464713165, 0.024762690879075525, 0.03745356995460173, 0.12133718530747008, 0.02259595542715642, 0.021667354519191086, 0.051176227816756084, 0.07325629385059843, 0.0023730912092447378, 0.007635163021048288, 0.05035080478745357, 0.025794469665703673, 0.07057366900536526, 0.07924061081304168, 0.01692117210070161, 0.0006190672719768881, 0.06510524143623607, 0.06634337598018984, 0.08574081716879901, 0.026826248452331822, 0.011555922410235245, 0.017952950887329757, 0.0023730912092447378, 0.02218324391250516, 0.0002063557573256294]

    lplist = []
    for i in range(26):
        ip = LetterProb(letter[i],occ[i])
        lplist.append(ip)

    # for i in range(26):
    #     print lplist[i].letter, lplist[i].prob

    print '-------------------start encoding--------------------------'
    
    '''
    Use huffman code
    '''
    print 'Result by hufman:'
    huffman(lplist)

    print '---------------------------------------------'
    '''
    Use shannon-Fano code for encoding
    li = [log(1/pi)]
    '''
    print 'Result by shannon fano:'
    shannonFano(lplist)





if __name__ == '__main__':
    main()