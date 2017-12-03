# ppy

#example
echo -e "aaa\nbbb" > hoge

cat hoge | xargs ./ppy.py "args.map('a*2')"
>aaaaaa
>bbbbbb

cat hoge | xargs ./ppy.py "args.reduce('a+b')"
aaabbb
