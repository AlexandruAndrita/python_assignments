import multiprocessing
import random
import argparse


def get_quarter_circle_hits(n: int)->int:
    quarter_hits=0
    while n:
        x_coordinate=random.random()
        y_coordinate=random.random()
        if x_coordinate**2+y_coordinate**2<1:
            quarter_hits+=1
        n-=1
    return quarter_hits


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--processes",type=int,default=1,required=False)
    parser.add_argument("-n","--n",type=int,default=1000,required=False)
    args=parser.parse_args()

    number_processes=args.processes
    n=args.n
    N=number_processes*n
    tmp=number_processes
    n_list=[]
    while tmp:
        n_list.append(n)
        tmp-=1
    C=0
    with multiprocessing.Pool(number_processes) as p:
        for return_value in p.imap(get_quarter_circle_hits,n_list):
            C=C+return_value

    pi_approximation=4*C/N

    print(f"{number_processes} processes with {n} checks each\ntotal tries: {N}\ntotal hits: {C}\npi approximation: {pi_approximation}")

