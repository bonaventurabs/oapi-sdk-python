# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchLocationAddressRequest = PatchLocationAddressRequest.builder() \
        .location_id("1616161616") \
        .address_id("1515151515") \
        .client_token("12454646") \
        .request_body(LocationAddressUpdate.builder()
                      .country_region_id("6862995757234914824")
                      .region_id("6863326264296474119")
                      .city_id("6863333555859097096")
                      .distinct_id("6863333556291110408")
                      .local_address_line1("丹佛测试地址-纽埃时区")
                      .local_address_line2("丹佛测试地址-纽埃时区")
                      .local_address_line3("丹佛测试地址-纽埃时区")
                      .local_address_line4("丹佛测试地址-纽埃时区")
                      .local_address_line5("丹佛测试地址-纽埃时区")
                      .local_address_line6("丹佛测试地址-纽埃时区")
                      .local_address_line7("丹佛测试地址-纽埃时区")
                      .local_address_line8("丹佛测试地址-纽埃时区")
                      .local_address_line9("丹佛测试地址-纽埃时区")
                      .postal_code("611530")
                      .address_types([])
                      .is_primary(True)
                      .is_public(True)
                      .build()) \
        .build()

    # 发起请求
    response: PatchLocationAddressResponse = client.corehr.v2.location_address.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.location_address.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchLocationAddressRequest = PatchLocationAddressRequest.builder() \
        .location_id("1616161616") \
        .address_id("1515151515") \
        .client_token("12454646") \
        .request_body(LocationAddressUpdate.builder()
                      .country_region_id("6862995757234914824")
                      .region_id("6863326264296474119")
                      .city_id("6863333555859097096")
                      .distinct_id("6863333556291110408")
                      .local_address_line1("丹佛测试地址-纽埃时区")
                      .local_address_line2("丹佛测试地址-纽埃时区")
                      .local_address_line3("丹佛测试地址-纽埃时区")
                      .local_address_line4("丹佛测试地址-纽埃时区")
                      .local_address_line5("丹佛测试地址-纽埃时区")
                      .local_address_line6("丹佛测试地址-纽埃时区")
                      .local_address_line7("丹佛测试地址-纽埃时区")
                      .local_address_line8("丹佛测试地址-纽埃时区")
                      .local_address_line9("丹佛测试地址-纽埃时区")
                      .postal_code("611530")
                      .address_types([])
                      .is_primary(True)
                      .is_public(True)
                      .build()) \
        .build()

    # 发起请求
    response: PatchLocationAddressResponse = await client.corehr.v2.location_address.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.location_address.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
