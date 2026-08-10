# 错误与误解日志

每个有意义的调试经验单独记录一项。复现代码应尽可能小；确认规则后，再用自己的话写下决定程序行为的规则。

## 记录边界

- 在学习单元步骤 1-4 中，本日志必须由学习者独立填写，Codex 不得帮助诊断、解释或修订。
- 首次独立提交之后，可以把 Codex 审阅发现补充到新条目中，但必须注明发现阶段和协助范围。
- 已有条目是学习证据，不应为了套用新模板而改写其事实内容。
- 每个修复都尽量对应一个能够防止复发的测试或断言。

## 2026-08-04 — 误以为整除结果会自动成为整数

### 现象

在判断表达式 `2 + 3 * 4 ** 2 / 8` 的结果类型时，预期结果为整数 `8`，但 Python 实际得到浮点数 `8.0`。

### 最小复现

```python
result = 48 / 8
print(result)
print(type(result))
```

### 错误假设

误以为当两个整数恰好整除时，Python 会根据结果没有小数部分而返回 `int`。

### 决定行为的规则

在 Python 3 中，运算符 `/` 执行真除法并返回 `float`，即使两个操作数都是整数且结果能够整除。`//` 执行向下取整除法，但其返回类型仍取决于操作数的类型。

### 修正

需要真除法时，接受并按浮点数处理 `/` 的结果。确实需要向下取整除法时使用 `//`；只有接口明确要求整数时，才在确认转换语义正确后使用 `int()`。

### 预防测试

```python
result = 48 / 8
assert result == 6.0
assert isinstance(result, float)
```

---

## 2026-08-04 — 忽略删除元素后列表索引会重新编号

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 3 章
- 发现阶段：第一次审阅
- 相关提交编号：`3bec041`
- Codex 参与情况：补充规则、修正方案和预防测试，并润色原记录

### 现象

本想依次删除列表中的前两个元素，却在第一次删除后继续使用原来的第二个索引，结果删除了错误的元素。类似写法在列表更短或删除次数更多时还可能引发 `IndexError`。

### 最小复现

```python
my_list = [1, 2, 3]

# 希望删除原列表中的 1 和 2。
del my_list[0]
del my_list[1]

print(my_list)  # [2]，实际删除的是 1 和 3。
```

### 错误假设

误以为删除一个元素后，其余元素仍保留原来的索引。

### 决定行为的规则

列表是连续的可变序列。执行 `del my_list[index]` 后，目标元素会被删除，位于它后面的元素会向左移动一位，并按当前位置重新编号。因此，第一次执行 `del my_list[0]` 后，原来索引为 `1` 的元素会变成新的索引 `0`。

### 修正

如果意图是删除开头连续的两个元素，可以直接删除切片：

```python
del my_list[:2]
```

### 预防测试

```python
my_list = [1, 2, 3]
del my_list[:2]
assert my_list == [3]
```

---

## 2026-08-04 — 误以为 `insert()` 的越界索引会引发 `IndexError`

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 3 章
- 发现阶段：闭卷检验
- 相关提交编号：`c2165ff`
- Codex 参与情况：Codex 设计并批改小测，随后根据小测答案整理本条目

### 现象

在闭卷判断 `items.insert(99, 4)` 的行为时，误答为抛出 `IndexError`。

### 最小复现

```python
items = [1, 2, 3]
result = items.insert(99, 4)
print(items)   # [1, 2, 3, 4]
print(result)  # None
```

### 错误假设

误以为 `list.insert(index, element)` 与按索引读取或删除元素一样，索引超出列表范围时都会抛出 `IndexError`。

### 决定行为的规则

`insert()` 会把索引调整到有效的插入边界：过大的正索引等同于在列表末尾插入，过小的负索引等同于在列表开头插入。它原地修改列表并返回 `None`。这与 `items[index]`、`del items[index]` 等要求索引指向已有元素的操作不同。

### 修正

不能只根据“索引越界”判断所有列表操作都会失败；需要区分访问已有元素和指定插入位置。预测 `insert()` 的结果时，同时检查修改后的列表和返回值。

### 预防测试

```python
items = [1, 2, 3]
result = items.insert(99, 4)
assert items == [1, 2, 3, 4]
assert result is None

items = [1, 2, 3]
items.insert(-99, 0)
assert items == [0, 1, 2, 3]
```

---

## 2026-08-04 — 混淆列表方法的返回值与运行时异常

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 3 章
- 发现阶段：闭卷检验
- 相关提交编号：`c2165ff`
- Codex 参与情况：Codex 设计并批改小测，随后根据小测答案整理本条目

### 现象

闭卷小测中，能够判断 `remove(8)` 会因列表中不存在 `8` 而失败，但没有识别出异常类型为 `ValueError`；同时误以为对非空列表执行合法的 `pop()` 会产生 `SyntaxError`。回答中还使用了“返回错误”的说法，混淆了返回值与抛出异常。

### 最小复现

```python
items = [1, 2, 3]
removed = items.pop()
print(removed)  # 3
print(items)    # [1, 2]

items = [1, 2, 3]
items.remove(8)  # 抛出 ValueError
```

### 错误假设

误以为 `pop()` 本身存在语法问题，并且没有区分正常返回一个值、返回 `None` 与抛出异常这三种不同结果。

### 决定行为的规则

- `pop()` 是合法的方法调用。对非空列表执行不带参数的 `pop()`，会删除并返回最后一个元素；对空列表执行则抛出 `IndexError`。
- `remove(value)` 按值删除第一个匹配元素，并在成功时返回 `None`；找不到该值时抛出 `ValueError`。
- `SyntaxError` 表示代码不符合 Python 语法，通常在代码开始执行前被发现。`ValueError` 和 `IndexError` 是代码执行过程中因值或索引不合要求而抛出的运行时异常。
- 返回值由调用表达式正常产生；异常会中断当前正常执行流程。因此应说“返回某个值”或“抛出某种异常”，而不是“返回异常”。

### 修正

判断方法调用时依次检查：语法是否合法、正常输入下修改了什么、正常返回值是什么，以及什么条件会抛出哪种异常。

### 预防测试

```python
import pytest

items = [1, 2, 3]
removed = items.pop()
assert removed == 3
assert items == [1, 2]

with pytest.raises(ValueError):
    items.remove(8)

with pytest.raises(IndexError):
    [].pop()
```

---

## 2026-08-11 — 误以为 `range()` 会直接创建列表

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 4 章
- 发现阶段：第一次审阅
- 相关提交编号：`e858041`
- Codex 参与情况：Codex 只读审阅时指出错误，学习者随后自行修正笔记

### 现象

笔记最初将 `range()` 描述为“创建等差数列构成的列表”。实际上，Python 3 中的 `range()` 返回 `range` 对象，而不是 `list`。

### 最小复现

```python
numbers = range(1, 4)
print(numbers)        # range(1, 4)
print(type(numbers))  # <class 'range'>
```

### 错误假设

误以为能够按顺序提供多个值的对象就是列表，并把 `range()` 产生的可迭代序列与由这些值构成的列表混为一谈。

### 决定行为的规则

`range()` 返回不可变的 `range` 序列对象。它可以被遍历、索引和切片，但不是列表，也不提供 `append()` 等列表修改方法。只有显式调用 `list(range(...))` 才会根据该范围创建列表。

### 修正

需要遍历整数范围时直接使用 `range()`；只有确实需要列表对象或列表方法时，才使用 `list(range(...))`。

### 预防测试

```python
numbers = range(1, 4)
assert isinstance(numbers, range)
assert not isinstance(numbers, list)
assert list(numbers) == [1, 2, 3]
```

---

## 2026-08-11 — 混淆列表别名、重新绑定与浅复制

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 4 章
- 发现阶段：第一次审阅后的讨论与第二次审阅
- 相关提交编号：`e858041`（原始学习成果；后续修正尚未提交）
- Codex 参与情况：Codex 只读审阅并解释对象、变量绑定和浅复制；学习者自行修改笔记和示例

### 现象

笔记最初把 `new_list = old_list` 当作一种列表复制，并认为使用 `old_list[:]` 后，无论如何修改其中一份列表都不会影响另一份。讨论“重新赋值”时，还一度误以为单独执行 `old_list = [1]` 会自动改变 `new_list`。

### 最小复现

```python
old_list = [1]
new_list = old_list

old_list.append(2)
print(new_list)  # [1, 2]：两个变量指向同一个列表

old_list = [100]
print(old_list)  # [100]
print(new_list)  # [1, 2]：重新绑定 old_list 不会改变 new_list 的指向
```

浅复制对嵌套可变对象仍然可能共享内部状态：

```python
old_list = [[1]]
new_list = old_list[:]

old_list[0].append(2)
print(new_list)  # [[1, 2]]
```

### 错误假设

- 误以为赋值语句总会复制赋值号右侧的对象。
- 没有区分修改现有对象与让变量名重新指向另一个对象。
- 误以为切片复制会递归复制列表中的所有对象。

### 决定行为的规则

- `new_list = old_list` 不复制列表，而是让两个变量指向同一个列表对象；通过任一变量进行原地修改，都能通过另一个变量观察到。
- `old_list = [100]` 会创建新列表并重新绑定 `old_list`。它不会修改旧列表，也不会改变 `new_list` 的绑定。
- `old_list[:]` 创建新的外层列表，但属于浅复制；新旧外层列表中的对应元素仍可能指向同一个可变对象。
- `==` 比较值是否相等，`is` 判断是否为同一个对象。

### 修正

描述列表行为时，分别说明变量绑定、对象身份和是否原地修改。需要独立外层列表时可使用切片或 `list.copy()`；需要复制嵌套可变对象时，应先判断是否确实需要深复制及其语义。

### 预防测试

```python
old_list = [1]
alias = old_list
copied = old_list[:]

assert alias is old_list
assert copied == old_list
assert copied is not old_list

old_list.append(2)
assert alias == [1, 2]
assert copied == [1]

old_list = [100]
assert alias == [1, 2]
```

---

## 2026-08-11 — 混淆元组的语法与变量重新绑定

### 学习单元与发现阶段

- 对应章节或单元：《Python Crash Course》第 4 章
- 发现阶段：第二次审阅
- 相关提交编号：`e858041`（原始学习成果；后续修正尚未提交）
- Codex 参与情况：Codex 只读审阅时指出错误，学习者随后自行修正元组的定义

### 现象

笔记最初认为圆括号是元组的决定性标志，并把变量改为指向另一个元组描述成“修改元组的值”。

### 最小复现

```python
not_a_tuple = (1)
one_item_tuple = (1,)
tuple_without_parentheses = 1, 2

print(type(not_a_tuple))              # <class 'int'>
print(type(one_item_tuple))           # <class 'tuple'>
print(type(tuple_without_parentheses))  # <class 'tuple'>
```

### 错误假设

误以为圆括号本身会创建元组，并误以为把变量重新赋值为另一个元组会修改原来的元组对象。

### 决定行为的规则

元组由逗号形成；圆括号通常用于分组和提高可读性。单元素元组必须包含尾随逗号。元组对象创建后不能给其中的位置重新赋值；执行 `my_tuple = (4, 5, 6)` 只是让变量 `my_tuple` 指向一个新元组，并没有修改原元组。

### 修正

创建单元素元组时写成 `(value,)`。描述后续赋值时使用“变量重新绑定到新元组”，而不是“修改原元组”。

### 预防测试

```python
assert not isinstance((1), tuple)
assert isinstance((1,), tuple)
assert isinstance((1, 2), tuple)

original = (1, 2, 3)
current = original
current = (4, 5, 6)
assert original == (1, 2, 3)
assert current == (4, 5, 6)
```

---



## YYYY-MM-DD — 简短标题

### 学习单元与发现阶段

- 对应章节或单元：
- 发现阶段：独立学习 / 第一次审阅 / 学习者修正 / 第二次审阅 / 闭卷检验
- 相关提交编号：
- Codex 参与情况：无 / 只读审阅 / 明确说明其他参与

### 现象


### 最小复现

```python
# 仍能展示问题的最小代码。
```

### 错误假设


### 决定行为的规则


### 修正


### 预防测试

```python
# 能够捕获该错误的回归测试或断言。
```
