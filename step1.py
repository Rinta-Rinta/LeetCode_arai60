step1
step1
ダブっているノードを消す。前のノードに戻れないので、一つの変数でダブりを確認するのは良くなさそう。
ここまではOKなノードを指す変数とここからチェック中を表す変数を用意する。
先頭からダブっている可能性が有るから、headとは別の先頭を指す変数を別に用意する。root_nodeにする。
あるノードがダブっているか確認するのを、どのように行うか考える。
まず次のノードと同じ値か確認する。
ダブっているなら、違う数字が出るか行き止まりになるかまでノードを飛ばし続ける。
行き止まりなら終了。違う数字ならそこからまたチェック開始。
これをまだチェックしていないノードに適応する。
ここまで考えたことを実装しようとしたが、出来なかった。
特に最初のノードがダブっていた時とダブってないときの動きを表現しようとしたときにノードを指す変数の動きが良くわからなくなってしまった。
書きかけのコード
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        root_node = head
        prev_node = head
        check_node = head

        if 
        while check_node.next is not None and check_node.val == check_node.next.val:
            check_node.next = check_node.next.next
```
araiさんの動画を見てみた。
一気に考えず、アルゴリズムを部分に分解して考える。
dummyのノードを用意するのは思いつかなかった。
それ以外の変数の動きは自分が考えていたものと似ていた。
動画で図を使った変数の動きを確認して、分かりやすかった。
考えるときに紙に書いて考えた方が分かりやすい。次から紙に書いて考える。
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        ptr = dummy

        while ptr.next is not None and ptr.next.next is not None:
            if ptr.next.val == ptr.next.next.val:
                copy = ptr.next
                while copy.next is not None and copy.val == copy.next.val:
                    copy = copy.next
                
                ptr.next = copy.next
            else:
                ptr = ptr.next
        
        return dummy.next
```
