# BFS
幅優先探索で迷路の最短経路を求めるアルゴリズム

## 入力
大きさNxMの迷路が次の形式で渡される。

```
10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
```
## 出力
スタート`'S'`からゴール`'G'`まで通路`'.'`を通って行く時の最短経路長を出力。