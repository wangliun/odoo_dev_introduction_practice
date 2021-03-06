# -*- coding: utf-8 -*-
###############################################################################
#
#
#
#
#
#
###############################################################################

from . const import Const

class GoodsRecommendStatus(Const):
    normal = (False, u'普通')
    recommend = (True, u'推荐')


class OrderStatus(Const):
    closed = ('closed', u'已关闭')
    unpaid = ('unpaid', u'待支付')
    pending = ('pending', u'待发货')
    unconfirmed = ('unconfirmed', u'待收货')
    unevaluated = ('unevaluated', u'待评价')
    completed = ('completed', u'已完成')

class OrderRequestStatus(Const):
    closed = (-1, 'closed')
    unpaid = (0, 'unpaid')
    pending = (1, 'pending')
    unconfirmed = (2, 'unconfirmed')
    unevaluated = (3, 'unevaluated')
    completed = (4, 'completed')

class OrderResponseStatus(Const):
    closed = ('closed', -1)
    unpaid = ('unpaid', 0)
    pending = ('pending', 1)
    unconfirmed = ('unconfirmed', 2)
    unevaluated = ('unevaluated', 3)
    completed = ('completed', 4)


class BannerStatus(Const):
    visible = (True, u'显示')
    invisible = (False, u'不显示')

class WechatUserRegisterType(Const):
    app = ('app', u'小程序')

class WechatUserStatus(Const):
    default = ('default', u'默认')

class PaymentStatus(Const):
    unpaid = ('unpaid', '未支付')
    success = ('success', '成功')
    fail = ('fail', '失败')