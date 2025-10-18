def serialize_tbuyer(tbuyer_instance):
    return {
        "id": tbuyer_instance.id,
        "buyerid": tbuyer_instance.buyerid,
        "buyername": tbuyer_instance.buyername,
        "orderno": tbuyer_instance.orderno,
        "date": tbuyer_instance.date.isoformat() if tbuyer_instance.date else None,
        "guid": tbuyer_instance.guid,
        "refresh": tbuyer_instance.refresh,
    }