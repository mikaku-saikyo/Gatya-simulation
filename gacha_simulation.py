import random
import matplotlib.pyplot as plt

def complete_gacha(n):
    gacha_pool = [False] * n  # 初期状態では全てのガチャが未取得(False)
    attempts = 0
    
    while not all(gacha_pool):
        # ガチャを引く
        gacha_index = random.randint(0, n - 1)
        
        # ガチャの結果をチェックし、未取得の場合に取得済みにする
        if not gacha_pool[gacha_index]:
            gacha_pool[gacha_index] = True
        
        attempts += 1
    
    return attempts

def main():
    n = int(input("ガチャの種類数を入力してください: "))
    trials = int(input("試行回数を入力してください: "))
    
    all_attempts = []
    
    for _ in range(trials):
        attempts = complete_gacha(n)
        all_attempts.append(attempts)

    # ヒストグラムを描画
    plt.hist(all_attempts, bins=range(min(all_attempts), max(all_attempts) + 1, 1), edgecolor='black')
    plt.xlabel('ガチャを引く回数')
    plt.ylabel('試行回数')
    plt.title(f'{trials}回の試行結果のガチャ回数の分布')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
