# Dj_test2
### settings.py中的DATABASES配置数据库
Django不会自动生成数据库，所以要我们自己手动创建。
类型 描述
AutoField 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。
BooleanField 布尔字段，值为True或False。
NullBooleanField 支持Null、True、False三种值。
CharField(max_length=最大长度) 字符串。参数max_length表示最大字符个数。
TextField 大文本字段，一般超过4000个字符时使用。
IntegerField 整数
DecimalField(max_digits=None, decimal_places=None) 十进制浮点数。参数max_digits表示总位。参数decimal_places表示小数位数。价格、
FloatField(max_digits=None, decimal_places=None) 浮点数。2^x
DateField：([auto_now=False, auto_now_add=False]) 日期。1)参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。2) 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。3)参数auto_now_add和auto_now是相互排斥的，组合将会发生错误。
TimeField 时间，参数同DateField。
DateTimeField 日期时间，参数同DateField。
FileField 上传文件字段。
ImageField 继承于FileField，对上传的内容进行校验，确保是有效的图片。