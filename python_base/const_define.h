#ifndef __CONST_DEFINE_H__
#define __CONST_DEFINE_H__

/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////ҵ����///////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
///����
#define CN_CS_Normal '0'
///ֻ��ƽ��
#define CN_CS_Only_Close '1'
///���ɽ���
#define CN_CS_Stop '2'

///δ����
#define CN_IP_Not_Start '0'
///����
#define CN_IP_Started '1'
///ͣ��
#define CN_IP_Pause '2'
///����
#define CN_IP_Expired '3'

///����Ȩ
#define CN_OT_NotOptions '0'
///����
#define CN_OT_CallOptions '1'
///����
#define CN_OT_PutOptions '2'

///��
#define CN_PD_Net '1'
///��ͷ
#define CN_PD_Long '2'
///��ͷ
#define CN_PD_Short '3'

///����ǰ
#define CN_IS_Before_Trading '0'
///�ǽ���
#define CN_IS_No_Trading '1'
///��������
#define CN_IS_Continous '2'
///���Ͼ��۱���
#define CN_IS_Auction_Ordering '3'
///���Ͼ��ۼ۸�ƽ��
#define CN_IS_Auction_Balance '4'
///���Ͼ��۴��
#define CN_IS_Auction_Match '5'
///����
#define CN_IS_Closed '6'

///��
#define CN_D_Buy '0'
///��
#define CN_D_Sell '1'

///Ͷ��
#define CN_HF_NULL '1'
///��ֵ
#define CN_HF_Hedge '3'

///ǿƽ
#define CN_PS_Force '0'
///һ��
#define CN_PS_Normal '1'

///����
#define CN_AF_Cancel '0'
///�޸�
#define CN_AF_Modify '1'

///��ʼ
#define CN_TAF_START '0'
///����
#define CN_TAF_STOP '1'

///���ֲ�
#define CN_PT_Net '1'
///�ۺϳֲ�
#define CN_PT_Gross '2'

///��Ծ
#define CN_ES_Active '1'
///����Ծ
#define CN_ES_Non_Active '2'

///��̬
#define CN_PL_Dynamic '1'
///��̬
#define CN_PL_Static '2'

///��
#define CN_VM_None '0'
///�ٷֱ�
#define CN_VM_Percentage '1'
///����ֵ
#define CN_VM_Absolute '2'

///���
#define CN_RM_Out '1'
///��������
#define CN_RM_Round '2'
///����
#define CN_RM_In '3'
///�ض�
#define CN_RM_Trunc '4'

///���
#define CN_AT_Deposit '1'
///����
#define CN_AT_Withdraw '2'
///������
#define CN_AT_Fee '3'

///ֱ�ӱ���
#define CN_CIT_Normal_Type '1'
///�Զ�����
#define CN_CIT_AutoCancel_Type '2'
///�Զ���
#define CN_CIT_AutoSplit_Type '3'
///��η���
#define CN_CIT_MultiSend_Type '4'
///ʱ����
#define CN_CIT_DetectTime_Type '5'

///�����
#define CN_OPT_Any_Price '1'
///�޼�
#define CN_OPT_Limit_Price '2'
///���ż�
#define CN_OPT_Best_Price '3'

///����
#define CN_OF_Open '0'
///ƽ��
#define CN_OF_Close '1'
///ǿƽ
#define CN_OF_Force_Close '2'
///ƽ��
#define CN_OF_Close_Today '3'
///ƽ��
#define CN_OF_Close_Yesterday '4'

///ȫ���ɽ�
#define CN_OST_All_Traded '0'
///���ֳɽ����ڶ�����
#define CN_OST_Part_Traded_Queueing '1'
///���ֳɽ����ڶ�����
#define CN_OST_Part_Traded_Not_Queueing '2'
///δ�ɽ����ڶ�����
#define CN_OST_No_Trade_Queueing '3'
///δ�ɽ����ڶ�����
#define CN_OST_No_Trade_Not_Queueing '4'
///����
#define CN_OST_Canceled '5'
///δ֪
#define CN_OST_Unknown 'a'
///��δ����
#define CN_OST_NotTouched 'b'
///�Ѵ���
#define CN_OST_Touched 'c'

///�������_������
#define CN_TC_IOC '1'
///������Ч
#define CN_TC_GFS '2'
///������Ч
#define CN_TC_GFD '3'
///ָ������ǰ��Ч
#define CN_TC_GTD '4'
///����ǰ��Ч
#define CN_TC_GTC '5'
///���Ͼ�����Ч
#define CN_TC_GFA '6'

///�κ�����
#define CN_VC_AV '1'
///��С����
#define CN_VC_MV '2'
///ȫ������
#define CN_VC_CV '3'

///����
#define CN_CC_Immediately '1'
///ֹ��
#define CN_CC_Touch '2'

///�û�
#define CN_AS_User '0'
///�ڲ�
#define CN_AS_Internal '1'
///����Ա
#define CN_AS_Administrator '2'

///���Խ���
#define CN_TR_Allow '0'
///ֻ��ƽ��
#define CN_TR_Close_Only '1'
///���ܽ���
#define CN_TR_Forbidden '2'

///�۸�����ʱ������
#define CN_TM_Price_Time '0'
///�۸����Ȱ���������
#define CN_TM_Prorata '1'

///���Բ�����
#define CN_OSRC_Participant '0'
///���Թ���Ա
#define CN_OSRC_Administrator '1'

///����״̬
#define CN_ACCS_Enable '0'
///ֹͣ״̬
#define CN_ACCS_Disable '1'

///�ڻ�
#define CN_ACCT_Domestic_Future '0'
///�ֻ�
#define CN_ACCT_Domestic_Stock '1'
///�ڻ�
#define CN_ACCT_international_Future '2'

///����
#define CN_IK_Key 'T'
///������
#define CN_IK_Not_Key 'F'

///�ֶ�Ϊ��
#define CN_IN_Null 'T'
///�ֶηǿ�
#define CN_IN_Not_Null 'F'

///δ����
#define CN_OS_Not_Connected '0'
///����δ����
#define CN_OS_Connected_Not_Work '1'
///��������
#define CN_OS_Work '2'

///�ϳ�δȷ��
#define CN_MIUS_Not_Confirm '0'
///�ϳ���ȷ��
#define CN_MIUS_Confirm_OK '1'
///�ϳ�ʧ��
#define CN_MIUS_Confirm_Error '2'

///��¼
#define CN_OT_Login '0'
///�ǳ�
#define CN_OT_Logout '1'
///����
#define CN_OT_Operate '2'

///����
#define CN_AT_Quote '0'
///����
#define CN_AT_Trade '1'

///����
#define CN_SO_Subscribe '1'
///�˶�
#define CN_SO_Unsubscribe '0'

///��ʼ����
#define CN_TCS_Start_Connect '0'
///���ӳɹ�
#define CN_TCS_Connected '1'
///���ӶϿ�
#define CN_TCS_Lose_Connect '2'

///�ڻ�
#define CN_VC_Futures '1'
///��Ȩ
#define CN_VC_Options '2'
///���
#define CN_VC_Combination '3'
///����
#define CN_VC_Spot '4'
///��ת��
#define CN_VC_EFP '5'

///����
#define CN_CT_Spread '0'
///��Ʒ��
#define CN_CT_Spread_Variety '1'
///ѹե����
#define CN_CT_Crush_Spread '2'
///չ��
#define CN_CT_Extension '3'

///һ�㵥��
#define CN_OT_Normal_Single '0'
///�������
#define CN_OT_Combination '1'
///��ⵥ��
#define CN_OT_Detect_Single '8'
///���Ե���
#define CN_OT_Test_Single '9'

///����
#define CN_RM_Normal '0'
///����
#define CN_RM_High_Speed '1'

///׼��
#define CN_DAT_Prepare '0'
///��ʼ
#define CN_DAT_Start '1'
///����
#define CN_DAT_End '2'

///δ��ʱ
#define CN_DTS_Not_Detect '0'
///��ʱʧ��
#define CN_DTS_Detect_Faild '1'
///��ʱ�ɹ�
#define CN_DTS_Detect_Ok '2'


/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////����Ŷ���/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
#define  MANAGE_SERVER_ID             1000  //�������
#define  RISK_SERVER_ID               2000  //���з�ط���


/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////��������ָ��///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
#define MANAGE_USER_LOGIN_COMMAND           1            //�����û���½
#define MANAGE_USER_LOGOUT_COMMAND          2            //�����û��ǳ�
#define TRADER_USER_LOGIN_COMMAND           3            //�����û���½
#define TRADER_USER_LOGOUT_COMMAND          4            //�����û��ǳ�

// �����������
#define ADD_ST_EXCHANGE_COMMAND		5  //����[��������]
#define DEL_ST_EXCHANGE_COMMAND		6  //ɾ��[��������]
#define UPD_ST_EXCHANGE_COMMAND		7  //�޸�[��������]
#define QRY_ST_EXCHANGE_COMMAND		8  //��ѯ[��������]

// ��Լ״̬�����
#define ADD_ST_INSTRUMENT_STATUS_COMMAND		9  //����[��Լ״̬��]
#define DEL_ST_INSTRUMENT_STATUS_COMMAND		10  //ɾ��[��Լ״̬��]
#define UPD_ST_INSTRUMENT_STATUS_COMMAND		11  //�޸�[��Լ״̬��]
#define QRY_ST_INSTRUMENT_STATUS_COMMAND		12  //��ѯ[��Լ״̬��]

// ��Լ�����
#define ADD_ST_INSTRUMENT_COMMAND		13  //����[��Լ��]
#define DEL_ST_INSTRUMENT_COMMAND		14  //ɾ��[��Լ��]
#define UPD_ST_INSTRUMENT_COMMAND		15  //�޸�[��Լ��]
#define QRY_ST_INSTRUMENT_COMMAND		16  //��ѯ[��Լ��]

// ��Լ��֤�������ѱ����
#define ADD_ST_INSTRUMENT_COMMISSION_MARGIN_COMMAND		17  //����[��Լ��֤�������ѱ�]
#define DEL_ST_INSTRUMENT_COMMISSION_MARGIN_COMMAND		18  //ɾ��[��Լ��֤�������ѱ�]
#define UPD_ST_INSTRUMENT_COMMISSION_MARGIN_COMMAND		19  //�޸�[��Լ��֤�������ѱ�]
#define QRY_ST_INSTRUMENT_COMMISSION_MARGIN_COMMAND		20  //��ѯ[��Լ��֤�������ѱ�]

// ��Լ�̶������ѱ�֤������
#define ADD_ST_FIX_INSTRUMENT_COMMISSION_MARGIN_COMMAND		21  //����[��Լ�̶������ѱ�֤���]
#define DEL_ST_FIX_INSTRUMENT_COMMISSION_MARGIN_COMMAND		22  //ɾ��[��Լ�̶������ѱ�֤���]
#define UPD_ST_FIX_INSTRUMENT_COMMISSION_MARGIN_COMMAND		23  //�޸�[��Լ�̶������ѱ�֤���]
#define QRY_ST_FIX_INSTRUMENT_COMMISSION_MARGIN_COMMAND		24  //��ѯ[��Լ�̶������ѱ�֤���]

// �����������
#define ADD_ST_BEST_MARKET_DATA_COMMAND		25  //����[��������]
#define DEL_ST_BEST_MARKET_DATA_COMMAND		26  //ɾ��[��������]
#define UPD_ST_BEST_MARKET_DATA_COMMAND		27  //�޸�[��������]
#define QRY_ST_BEST_MARKET_DATA_COMMAND		28  //��ѯ[��������]

// ί�б����
#define ADD_ST_ORDER_COMMAND		29  //����[ί�б�]
#define DEL_ST_ORDER_COMMAND		30  //ɾ��[ί�б�]
#define UPD_ST_ORDER_COMMAND		31  //�޸�[ί�б�]
#define QRY_ST_ORDER_COMMAND		32  //��ѯ[ί�б�]

// �ɽ������
#define ADD_ST_TRADE_COMMAND		33  //����[�ɽ���]
#define DEL_ST_TRADE_COMMAND		34  //ɾ��[�ɽ���]
#define UPD_ST_TRADE_COMMAND		35  //�޸�[�ɽ���]
#define QRY_ST_TRADE_COMMAND		36  //��ѯ[�ɽ���]

// �ֲֻ��ܱ����
#define ADD_ST_POSITION_COMMAND		37  //����[�ֲֻ��ܱ�]
#define DEL_ST_POSITION_COMMAND		38  //ɾ��[�ֲֻ��ܱ�]
#define UPD_ST_POSITION_COMMAND		39  //�޸�[�ֲֻ��ܱ�]
#define QRY_ST_POSITION_COMMAND		40  //��ѯ[�ֲֻ��ܱ�]

// �ʽ���Ϣ�����
#define ADD_ST_MONEY_COMMAND		41  //����[�ʽ���Ϣ��]
#define DEL_ST_MONEY_COMMAND		42  //ɾ��[�ʽ���Ϣ��]
#define UPD_ST_MONEY_COMMAND		43  //�޸�[�ʽ���Ϣ��]
#define QRY_ST_MONEY_COMMAND		44  //��ѯ[�ʽ���Ϣ��]

// ����Ա�����
#define ADD_ST_MANAGE_USER_COMMAND		45  //����[����Ա��]
#define DEL_ST_MANAGE_USER_COMMAND		46  //ɾ��[����Ա��]
#define UPD_ST_MANAGE_USER_COMMAND		47  //�޸�[����Ա��]
#define QRY_ST_MANAGE_USER_COMMAND		48  //��ѯ[����Ա��]

// ����Ա�����
#define ADD_ST_TRADE_USER_COMMAND		49  //����[����Ա��]
#define DEL_ST_TRADE_USER_COMMAND		50  //ɾ��[����Ա��]
#define UPD_ST_TRADE_USER_COMMAND		51  //�޸�[����Ա��]
#define QRY_ST_TRADE_USER_COMMAND		52  //��ѯ[����Ա��]

// �û���¼��Ϣ�����
#define ADD_ST_USER_LOGIN_COMMAND		53  //����[�û���¼��Ϣ��]
#define DEL_ST_USER_LOGIN_COMMAND		54  //ɾ��[�û���¼��Ϣ��]
#define UPD_ST_USER_LOGIN_COMMAND		55  //�޸�[�û���¼��Ϣ��]
#define QRY_ST_USER_LOGIN_COMMAND		56  //��ѯ[�û���¼��Ϣ��]

// ����Ա������Ա����
#define ADD_ST_TRADER_BROKER_STRATEGY_COMMAND		57  //����[����Ա������Ա�]
#define DEL_ST_TRADER_BROKER_STRATEGY_COMMAND		58  //ɾ��[����Ա������Ա�]
#define UPD_ST_TRADER_BROKER_STRATEGY_COMMAND		59  //�޸�[����Ա������Ա�]
#define QRY_ST_TRADER_BROKER_STRATEGY_COMMAND		60  //��ѯ[����Ա������Ա�]

// ���Բ��������
#define ADD_ST_STRATEGY_PARA_COMMAND		61  //����[���Բ�����]
#define DEL_ST_STRATEGY_PARA_COMMAND		62  //ɾ��[���Բ�����]
#define UPD_ST_STRATEGY_PARA_COMMAND		63  //�޸�[���Բ�����]
#define QRY_ST_STRATEGY_PARA_COMMAND		64  //��ѯ[���Բ�����]

// ����۱����
#define ADD_ST_CLOSE_PRICE_COMMAND		65  //����[����۱�]
#define DEL_ST_CLOSE_PRICE_COMMAND		66  //ɾ��[����۱�]
#define UPD_ST_CLOSE_PRICE_COMMAND		67  //�޸�[����۱�]
#define QRY_ST_CLOSE_PRICE_COMMAND		68  //��ѯ[����۱�]

// �������������
#define ADD_ST_TRADE_CALENDAR_COMMAND		69  //����[����������]
#define DEL_ST_TRADE_CALENDAR_COMMAND		70  //ɾ��[����������]
#define UPD_ST_TRADE_CALENDAR_COMMAND		71  //�޸�[����������]
#define QRY_ST_TRADE_CALENDAR_COMMAND		72  //��ѯ[����������]

// ���ײ��������
#define ADD_ST_TRADE_PARA_COMMAND		73  //����[���ײ�����]
#define DEL_ST_TRADE_PARA_COMMAND		74  //ɾ��[���ײ�����]
#define UPD_ST_TRADE_PARA_COMMAND		75  //�޸�[���ײ�����]
#define QRY_ST_TRADE_PARA_COMMAND		76  //��ѯ[���ײ�����]


/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////�������ָ��///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
#define TRADE_MARKET_CONNECTED_COMMAND		77  //�������ӳɹ�   
#define TRADE_MARKET_DISCONNECT_COMMAND		78  //��������ʧ��   
#define TRADE_RTN_MARKET_DATA_COMMAND		79  //�������֪ͨ   
#define TRADE_OFFER_AVAILABLE_COMMAND		80  //���̿���
#define TRADE_OFFER_UNAVAILABLE_COMMAND		81  //���̲�����   
#define TRADE_RSP_INSERT_ORDER_COMMAND		82  //����Ӧ��   
#define TRADE_RSP_ORDER_ACTION_COMMAND		83  //��������Ӧ��   
#define TRADE_RTN_ORDER_COMMAND		84  //�����ر�   
#define TRADE_RTN_TRADE_COMMAND		85  //�ɽ��ر�   
#define TRADE_RTN_INSTRUMENT_STATUS_COMMAND		86  //��Լ״̬֪ͨ   
#define TRADE_RSP_QRY_INSTRUMENT_COMMAND		87  //��Լ��ѯӦ��   
#define TRADE_REQ_ORDER_INSERT_COMMAND		88  //��������   
#define TRADE_REQ_ORDER_ACTION_COMMAND		89  //������������   
#define TRADE_CHANGE_STRATEGY_PARAM		90  //�������Բ���   
#define TRADE_RTN_MONERY_COMMAND		91  //�ʽ�֪ͨ   
#define TRADE_RTN_POSITION_COMMAND		92  //�ֲֻ���֪ͨ   

/////////////////////////////////////////////////////////////////////////////////////////
//////////////////////�ṹ��FIELD���////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
#define ST_RSP_INFO_FIELD		1  //Ӧ����Ϣ��
#define ST_EXCHANGE_FIELD		2  //����������
#define ST_INSTRUMENT_STATUS_FIELD		3  //��Լ״̬����
#define ST_INSTRUMENT_FIELD		4  //��Լ����
#define ST_INSTRUMENT_COMMISSION_MARGIN_FIELD		5  //��Լ��֤�������ѱ���
#define ST_FIX_INSTRUMENT_COMMISSION_MARGIN_FIELD		6  //��Լ�̶������ѱ�֤�����
#define ST_BEST_MARKET_DATA_FIELD		7  //����������
#define ST_ORDER_FIELD		8  //ί�б���
#define ST_TRADE_FIELD		9  //�ɽ�����
#define ST_POSITION_FIELD		10  //�ֲֻ��ܱ���
#define ST_MONEY_FIELD		11  //�ʽ���Ϣ����
#define ST_MANAGE_USER_FIELD		12  //����Ա����
#define ST_TRADE_USER_FIELD		13  //����Ա����
#define ST_USER_LOGIN_FIELD		14  //�û���¼��Ϣ����
#define ST_TRADER_BROKER_STRATEGY_FIELD		15  //����Ա������Ա���
#define ST_STRATEGY_PARA_FIELD		16  //���Բ�������
#define ST_CLOSE_PRICE_FIELD		17  //����۱���
#define ST_TRADE_CALENDAR_FIELD		18  //������������
#define ST_TRADE_PARA_FIELD		19  //���ײ�������

#endif
