from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name','doctor_name', 'create_time')

    # 需要搜索的字段
    search_fields = ('name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True





@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    #resource_class = ProxyResource
    list_display = ( 'name', 'gender', 'phone', 'stu_no','department', 'enable', 'create_time','idCard')
    # search_fields = ('name', 'enable', 'idCard', 'department')
    search_fields = ('name', 'phone')
    list_per_page = 20
    # raw_id_fields = ('department',)
    # list_filter = ('department', AgeListFilter, 'create_time')
    # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')

    list_display_links = ('name',)


    #fields = ('user_name', 'idCard', 'birthday')  # 编辑界面只显示No、Name和Age

    #exclude = ('pass_word','user_name')  # 记得元祖需要在后面加个逗号，不然会报错

    list_editable = ('department', 'phone', 'enable', 'gender','idCard','stu_no')

    date_hierarchy = 'create_time'




@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('no', 'name','level','amount', 'create_time')

    fields = ('no', 'name', 'level','amount' )  # 编辑界面只显示No、Name和Age

    # 需要搜索的字段
    search_fields = ('no',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True

    # inlines = [
    #     HealthLogInline,
    #     MaintanceInline
    # ]

import xlwt
from django.http import HttpResponse, JsonResponse
import datetime

@admin.register(Medical)
class MedicalAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name', 'price', 'qr_code', 'create_time', 'prescription')

    fields = ('name', 'qr_code', 'price', 'prescription')  # 编辑界面只显示No、Name和Age
    actions = ['output']
    # 需要搜索的字段
    search_fields = ('name', 'qr_code', 'price', 'prescription')

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True

    # inlines = [
    #     HealthLogInline,
    #     MaintanceInline
    # ]

    def output(self, request, queryset):
        response = HttpResponse(
            content_type='application/vnd.ms-excel')  # 指定返回格式为excel，excel文件MINETYPE为application/vnd.ms-excel
        response['Content-Disposition'] = 'attachment;filename=instorage.xls'
        wb = xlwt.Workbook(encoding='utf-8')  # 创建一个工作簿
        sheet = wb.add_sheet('药品单据')  # 创建一个工作表
        # 创建一个居中对齐的样式
        style = xlwt.XFStyle()
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        style.alignment = alignment
        font = xlwt.Font()
        font.name = '宋体'
        font.bold = True
        font.height = 20 * 11  # 设置字体大小
        style.font = font

        # 将样式应用于单元格
        sheet.write_merge(0, 0, 0, 5, '药品单据', style)
        sheet.write(1, 0, 'id', style)
        sheet.write(1, 1, '名称', style)
        sheet.write(1, 2, '描述', style)
        sheet.write(1, 3, '价格', style)
        sheet.write(1, 4, '数量', style)
        sheet.write(1, 5, '创建时间', style)
        data_row = 2
        for obj in queryset:
            # 创建一个居中对齐的样式
            style = xlwt.XFStyle()
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            style.alignment = alignment

            sheet.write(data_row, 0, obj.id, style)
            sheet.write(data_row, 1, obj.name, style)
            sheet.write(data_row, 2, obj.prescription, style)
            sheet.write(data_row, 3, str(obj.price), style)
            sheet.write(data_row, 4, obj.qr_code, style)
            sheet.write(data_row, 5, obj.create_time.strftime('%Y-%m-%d'), style)
            data_row = data_row + 1
        wb.save(response)
        return response

    output.short_description = '生成药品单据'
    output.type = 'success'
    output.style = 'background-color: #00a65a; color: #fff; border-color: #008d4c;'






@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    #resource_class = ProxyResource
    list_display = ( 'name', 'gender', 'phone', 'idCard','department', 'in_time','doctor_name', 'create_time','idCard')
    # search_fields = ('name', 'enable', 'idCard', 'department')
    search_fields = ('name', 'department__name')
    list_per_page = 20
    # raw_id_fields = ('department',)
    # list_filter = ('department', AgeListFilter, 'create_time')
    # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')

    list_display_links = ('name',)


    #fields = ('user_name', 'idCard', 'birthday')  # 编辑界面只显示No、Name和Age

    #exclude = ('pass_word','user_name')  # 记得元祖需要在后面加个逗号，不然会报错

    list_editable = ('department', 'phone', 'idCard', 'doctor_name', 'gender','idCard','in_time')

    date_hierarchy = 'create_time'