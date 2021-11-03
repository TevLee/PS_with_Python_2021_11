'''가방문제'''
# 13:07 -
import sys
sys.stdin = open("in1.txt","rt")

#최대 17kg
N,W = map(int,input().split()) # number, weight
js = [list(map(int,input().split())) for _ in range(N)]
## 이 보석 무게부터 dp 쭉보면서
## 현재무게의 가치 vs 이보석뺀무게의 현재가치 + 지금보석가치

