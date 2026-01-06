step1
訪れたノードのアドレスを記録しておき、同じアドレスが出てきたらサイクルがあると判断できると考えた。

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        check = head

        while check != None:
            if id(check) in visited:
                return True

            visited.append(id(check))

            check = check.next

        return False
```

解説の動画を見てみると知らない方法を使っていたのでそれも真似してみた。

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
```


step2
他の人のコードを読んでみた。
他の人の書いたコードを見てみると、リストを使っているのが自分しかおらず、他の人はsetを使っていた。
自分はなんとなくリストで書いた。
他の人がsetで書いている理由がわからなかったので、geminiに聞いてみた。
リストは要素の探索の際に線形探索を行うので、時間計算量がO(n^2)かかり、setではハッシュを使うので時間計算量はO(n)になると分かった。
空間計算量はどちらもO(n)だが、setでは衝突を防ぐためにリストより大きめにメモリを確保するらしい。
今回の問題ではノード数の上限は10^4だった
時間計算量は、リストの場合は10^4 ×　(10^4 - 1) / 2 = 50000000
setの時は10000
桁が3つ違うのでsetを使うことにした。
空間計算量は具体的にはどれくらいなのかgeminiに聞いてみた。
リストの場合は8バイト×10000ノードで80000バイトぐらい。
setの場合はハッシュ内の一つのスロットにキーとハッシュそれぞれで8バイト、計16バイト必要
占有率を最大でも2/3ぐらいにするために、10000×(3/2)スロット必要　　(ロードファクタというらしい。)
また、スロット数は2のべき乗個用意するらしい。
割り算で余りを求めなくても、ビット演算で余りが分かるから。
2^13<15000<2^14だから2^14個スロットを用意する
16バイト×2^14スロット=2^18バイト必要らしい
また、わざわざアドレスを調べなくても、変数名でインスタンスを参照できるので、id()はやめることにした。
現在見ているものを指すときはcurrが一般的な様なのでcheckではなく、currを使うようにした。
while文を　is notで書いている人がいた。
!=は値でis notはインスタンスを比較しているらしい。
今回はインスタンスが違うかを判定しているのでis notで書くことにした。

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = set()

        curr = head

        while curr is not None:
            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next

        return False
```
動画の方法も!=ではなくis notにしてみた

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        fast = head 
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True

        return False
```
step3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = set()

        curr = head

        while curr is not None:
            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next

        return False
```
動画の方法
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True

        return False
```
