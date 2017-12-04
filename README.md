# ppy

# example
echo -e "foo\nbar" > hoge
>foo<br>
>bar

cat hoge | xargs ./ppy.py "args.map('a*2')"
>foofoo</br>
>barbar

cat hoge | xargs ./ppy.py "args.reduce('a+b')"
>foobar

cat hoge | xargs ./ppy.py "args.filter(\\"'b' in a\\")"
>bar

cat hoge | xargs ./ppy.py "args.map('a+\\"qwer\\"').filter(\\"'b' in a\\")"
>barqwer
