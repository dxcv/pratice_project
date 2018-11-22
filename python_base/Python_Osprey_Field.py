## -*- coding: gb2312 -*

from python_base.Python_Data_Type import *

#��Ӧ��Ϣ
class CRsp_Info_Field:
    def __init__(self):
		#�������
		self.Error_ID = CError_ID_Type() 
		#������Ϣ
		self.Error_Msg = CError_Msg_Type() 

#�ͻ���¼
class CCustomer_Login_Field:
    def __init__(self):
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#����
		self.Password = CPassword_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.Customer_Order_Local_ID = COrder_Local_ID_Type() 

#�ͻ���¼�˳�
class CCustomer_Logout_Field:
    def __init__(self):
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#����
		self.Password = CPassword_Type() 

#ϵͳ�û���¼
class CSystem_User_Login_Field:
    def __init__(self):
		#�û�����
		self.System_User_ID = CSystem_User_ID_Type() 
		#����
		self.Password = CPassword_Type() 

#ϵͳ�û���¼�˳�
class CSystem_User_Logout_Field:
    def __init__(self):
		#�û�����
		self.System_User_ID = CSystem_User_ID_Type() 
		#����
		self.Password = CPassword_Type() 

#������������
class CExchange_Trading_Day_Field:
    def __init__(self):
		#���׷���������
		self.Trading_Day = CDate_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 

#������
class CExchange_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#����������
		self.Exchange_Name = CExchange_Name_Type() 

#ϵͳ�û�
class CSystem_User_Field:
    def __init__(self):
		#
		self.System_User_ID = CSystem_User_ID_Type() 
		#
		self.System_User_Name = CSystem_User_Name_Type() 
		#0��ϵͳ����Ա 1�������û� 2: ҵ�����Ա
		self.System_User_Type = CSystem_User_Type_Type() 
		#����
		self.Password = CPassword_Type() 
		#
		self.Is_Active = CBool_Type() 

#�ͻ�
class CCustomer_Field:
    def __init__(self):
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ�����
		self.Customer_Name = CParty_Name_Type() 
		#��Ȼ�ˣ�����
		self.Customer_Type = CCustomer_Type_Type() 
		#����
		self.Password = CPassword_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.Customer_Order_Local_ID = COrder_Local_ID_Type() 
		#������ֻ��ƽ�֣���ֹ����
		self.Customer_Status = CCustomer_Status_Type() 

#Ʒ��
class CVariety_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Ʒ����
		self.Variety_Name = CVariety_Name_Type() 
		#��Ʒ����
		self.Variety_ID = CVariety_ID_Type() 
		#Ʒ�ֵ�ÿ�ֽ��׵Ĺ涨��������Ի�������Ʒ
		self.Volume_Multiple = CVolume_Multiple_Type() 
		#�۸�С��λ
		self.Price_Decimal = CPrice_Decimal_Type() 
		#��Լ�ĵ�λ�۸��ǵ��仯����Сֵ
		self.Price_Tick = CPrice_Type() 
		#�г��۱���������µ���
		self.Max_Market_Order_Volume = CVolume_Type() 
		#�г��۱�������С�µ���
		self.Min_Market_Order_Volume = CVolume_Type() 
		#�޼۱���������µ���
		self.Max_Limit_Order_Volume = CVolume_Type() 
		#�޼۱�������С�µ���
		self.Min_Limit_Order_Volume = CVolume_Type() 
		#���ֲ���
		self.Max_Limit_Position_Volume = CVolume_Type() 
		#��֤����
		self.Margin_Rate = CRatio_Type() 
		#��������
		self.Fee_Rate = CRatio_Type() 
		#ƽ��������
		self.Offset_Today_Rate = CRatio_Type() 
		#�·ݱ�־
		self.Month_Flag = CMonth_Flag_Type() 

#��Լ��Ϣ
class CInstrument_Field:
    def __init__(self):
		#Ʒ����ϵͳ�еı��
		self.Variety_ID = CVariety_ID_Type() 
		#������Լ�ĳֲ�����
		self.Position_Type = CPosition_Type_Type() 
		#Ʒ�ֵ�ÿ�ֽ��׵Ĺ涨��������Ի�������Ʒ
		self.Volume_Multiple = CVolume_Multiple_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#��Լ������
		self.Instrument_Name = CInstrument_Name_Type() 
		#�ú�Լ�涨����ʵ�ｻ������
		self.Delivery_Year = CYear_Type() 
		#�ú�Լ�涨����ʵ�ｻ����·�
		self.Delivery_Month = CMonth_Type() 
		#�г��۱���������µ���
		self.Max_Market_Order_Volume = CVolume_Type() 
		#�г��۱�������С�µ���
		self.Min_Market_Order_Volume = CVolume_Type() 
		#�޼۱���������µ���
		self.Max_Limit_Order_Volume = CVolume_Type() 
		#�޼۱�������С�µ���
		self.Min_Limit_Order_Volume = CVolume_Type() 
		#���ֲ���
		self.Max_Limit_Position_Volume = CVolume_Type() 
		#��Լ�ĵ�λ�۸��ǵ��仯����Сֵ
		self.Price_Tick = CPrice_Type() 
		#��֤����
		self.Margin_Rate = CRatio_Type() 
		#��������
		self.Fee_Rate = CRatio_Type() 
		#ƽ��������
		self.Offset_Today_Rate = CRatio_Type() 

#��ǰʱ��
class CCurrent_Time_Field:
    def __init__(self):
		#��ǰ����
		self.Curr_Date = CDate_Type() 
		#Ŀǰ�ľ�ȷ�����ʱ��
		self.Curr_Time = CTime_Type() 
		#��ǰʱ�䣨���룩
		self.Curr_Millisec = CMillisec_Type() 

#���뱨��
class CInput_Order_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#�������
		self.Order_Sys_ID = COrder_Sys_ID_Type() 
		#ÿһλ��Ա��ϵͳ�еı��룬���Ψһ����ѭ�������ƶ��ı������
		self.Participant_ID = CParticipant_ID_Type() 
		#����Ա��ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Seat_ID = CSeat_ID_Type() 
		#�ͻ���ϵͳ�еı��
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ��ڸ���������ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�޼۵����м۵�
		self.Order_Price_Type = COrder_Price_Type_Type() 
		#1����2����
		self.Direction = CDirection_Type() 
		#��ƽ����
		self.Offset_Flag = COffset_Flag_Type() 
		#�ױ���־
		self.Hedge_Flag = CHedge_Flag_Type() 
		#�޼۵��۸�
		self.Limit_Price = CPrice_Type() 
		#��������
		self.Volume_Total_Original = CVolume_Type() 
		#IOC��GFS��GFD��GTD��GTC��GFA
		self.Time_Condition = CTime_Condition_Type() 
		#����ָ����֮ǰ������Ч������
		self.GTD_Date = CDate_Type() 
		#AV��MV��CV
		self.Volume_Condition = CVolume_Condition_Type() 
		#���ɽ�������ΪMVʱ��Ч
		self.Min_Volume = CVolume_Type() 
		#1������2��ֹ��
		self.Contingent_Condition = CContingent_Condition_Type() 
		#�ڻ���Լ��������ʱ��Ϊ�˷�ֹ�����һ�����󣬽�����Ԥ���趨�Ĵ����޼�ƽ��ָ��ļ�λ��
		self.Stop_Price = CPrice_Type() 
		#ǿƽԭ��
		self.Force_Close_Reason = CForce_Close_Reason_Type() 
		#���ر���˳���
		self.Order_Local_ID = COrder_Local_ID_Type() 
		#�Զ������־
		self.Is_Auto_Suspend = CBool_Type() 
		#����ָ���,���ܶ�Ӧ�˶������
		self.Order_Local_Instruction_ID = COrder_Local_Instruction_ID_Type() 
		#����ָ������,������ָ���ִ�з�ʽ
		self.Order_Local_Instruction_Type = COrder_Local_Instruction_Type_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.System_User_Order_Local_ID = COrder_Local_ID_Type() 
		#Market�յ����ĵ�ʱ��
		self.Receive_Time = CTime_Type() 
		#�ͻ��˵�¼ʱʹ�õ�ϵͳ�û����ƣ�Ҳ�����ǿͻ���
		self.System_User_ID = CSystem_User_ID_Type() 
		#���̻��ĻỰID
		self.Offer_SessionID = COffer_SessionID_Type() 
		#IP��ַ
		self.IP_Address = CIP_Address_Type() 

#��������
class COrder_Action_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�������
		self.Order_Sys_ID = COrder_Sys_ID_Type() 
		#���ر������
		self.Order_Local_ID = COrder_Local_ID_Type() 
		#�������ر��
		self.Action_Local_ID = COrder_Local_ID_Type() 
		#������־
		self.Action_Flag = CAction_Flag_Type() 
		#�ͻ���ϵͳ�еı��
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#����Ա��ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Seat_ID = CSeat_ID_Type() 
		#�޼۵��۸�
		self.Limit_Price = CPrice_Type() 
		#���������仯
		self.Volume_Change = CVolume_Type() 
		#����ָ���,���ܶ�Ӧ�˶������
		self.Order_Local_Instruction_ID = COrder_Local_Instruction_ID_Type() 
		#����ָ������,������ָ���ִ�з�ʽ
		self.Order_Local_Instruction_Type = COrder_Local_Instruction_Type_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.System_User_Order_Local_ID = COrder_Local_ID_Type() 
		#�ͻ��˵�¼ʱʹ�õ�ϵͳ�û����ƣ�Ҳ�����ǿͻ���
		self.System_User_ID = CSystem_User_ID_Type() 
		#���̻��ĻỰID
		self.Offer_SessionID = COffer_SessionID_Type() 

#�ɽ�
class CTrade_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#����Ա��ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Seat_ID = CSeat_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#�ͻ���ϵͳ�еı��
		self.Customer_ID = CCustomer_ID_Type() 
		#�ɽ����
		self.Trade_ID = CTrade_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#1.��2.��
		self.Direction = CDirection_Type() 
		#1������2��ƽ��3��ƽ��4��ǿƽ
		self.Offset_Flag = COffset_Flag_Type() 
		#1.Ͷ��3.�ױ�
		self.Hedge_Flag = CHedge_Flag_Type() 
		#�������
		self.Order_Sys_ID = COrder_Sys_ID_Type() 
		#���ɽ���ʹ�õ��ʽ��ʻ�
		self.Account_ID = CAccount_ID_Type() 
		#�ɽ��۸�
		self.Price = CPrice_Type() 
		#�ɽ�����
		self.Volume = CVolume_Type() 
		#�ɽ�ʱ��
		self.Trade_Time = CTime_Type() 
		#�ɽ�����
		self.Trade_Type = CTrade_Type_Type() 
		#�ɽ�����Դ
		self.Price_Source = CPrice_Source_Type() 
		#���ر���˳���
		self.Order_Local_ID = COrder_Local_ID_Type() 

#����
class COrder_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#�������
		self.Order_Sys_ID = COrder_Sys_ID_Type() 
		#ÿһλ��Ա��ϵͳ�еı��룬���Ψһ����ѭ�������ƶ��ı������
		self.Participant_ID = CParticipant_ID_Type() 
		#����Ա��ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Seat_ID = CSeat_ID_Type() 
		#�ͻ���ϵͳ�еı��
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ��ڸ���������ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�޼۵����м۵�
		self.Order_Price_Type = COrder_Price_Type_Type() 
		#1����2����
		self.Direction = CDirection_Type() 
		#��ƽ����
		self.Offset_Flag = COffset_Flag_Type() 
		#�ױ���־
		self.Hedge_Flag = CHedge_Flag_Type() 
		#�޼۵��۸�
		self.Limit_Price = CPrice_Type() 
		#��������
		self.Volume_Total_Original = CVolume_Type() 
		#IOC��GFS��GFD��GTD��GTC��GFA
		self.Time_Condition = CTime_Condition_Type() 
		#����ָ����֮ǰ������Ч������
		self.GTD_Date = CDate_Type() 
		#AV��MV��CV
		self.Volume_Condition = CVolume_Condition_Type() 
		#���ɽ�������ΪMVʱ��Ч
		self.Min_Volume = CVolume_Type() 
		#1������2��ֹ��
		self.Contingent_Condition = CContingent_Condition_Type() 
		#�ڻ���Լ��������ʱ��Ϊ�˷�ֹ�����һ�����󣬽�����Ԥ���趨�Ĵ����޼�ƽ��ָ��ļ�λ��
		self.Stop_Price = CPrice_Type() 
		#ǿƽԭ��
		self.Force_Close_Reason = CForce_Close_Reason_Type() 
		#���ر���˳���
		self.Order_Local_ID = COrder_Local_ID_Type() 
		#�Զ������־
		self.Is_Auto_Suspend = CBool_Type() 
		#����ָ���,���ܶ�Ӧ�˶������
		self.Order_Local_Instruction_ID = COrder_Local_Instruction_ID_Type() 
		#����ָ������,������ָ���ִ�з�ʽ
		self.Order_Local_Instruction_Type = COrder_Local_Instruction_Type_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.System_User_Order_Local_ID = COrder_Local_ID_Type() 
		#Market�յ����ĵ�ʱ��
		self.Receive_Time = CTime_Type() 
		#�ͻ��˵�¼ʱʹ�õ�ϵͳ�û����ƣ�Ҳ�����ǿͻ���
		self.System_User_ID = CSystem_User_ID_Type() 
		#���̻��ĻỰID
		self.Offer_SessionID = COffer_SessionID_Type() 
		#IP��ַ
		self.IP_Address = CIP_Address_Type() 
		#������Դ
		self.Order_Source = COrder_Source_Type() 
		#0��ȫ���ɽ�1�����ֳɽ����ڶ�����2�����ֳɽ����ڶ�����3��δ�ɽ����ڶ�����4��δ�ɽ����ڶ�����5������
		self.Order_Status = COrder_Status_Type() 
		#�����������
		self.Volume_Traded = CVolume_Type() 
		#����δ�������
		self.Volume_Total = CVolume_Type() 
		#��������
		self.Insert_Date = CDate_Type() 
		#����ʱ��
		self.Insert_Time = CTime_Type() 
		#����ʱ��
		self.Active_Time = CTime_Type() 
		#����ʱ��
		self.Suspend_Time = CTime_Type() 
		#����޸�ʱ��
		self.Update_Time = CTime_Type() 
		#����ʱ��
		self.Cancel_Time = CTime_Type() 
		#������Ϣ
		self.Error_Msg = CError_Msg_Type() 
		#����������
		self.Frzn_Commi = CMoney_Type() 
		#���ᱣ֤��
		self.Frzn_Margin = CMoney_Type() 
		#��Ʒ����
		self.Variety_ID = CVariety_ID_Type() 
		#�ú�Լ�涨����ʵ�ｻ����·�
		self.Delivery_Month = CMonth_Type() 

#�ͻ��ʽ��ʻ����
class CAccount_Deposit_Field:
    def __init__(self):
		#�ʽ��˺�
		self.Account_ID = CAccount_ID_Type() 
		#�����
		self.Deposit = CMoney_Type() 

#��������
class CBest_Market_Data_Field:
    def __init__(self):
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 
		#����޸�ʱ��
		self.Update_Time = CTime_Type() 
		#����޸ĺ���
		self.Update_Millisec = CMillisec_Type() 
		#������
		self.Trading_Day = CDate_Type() 
		#�����
		self.Pre_Settlement_Price = CPrice_Type() 
		#������
		self.Pre_Close_Price = CPrice_Type() 
		#��ֲ���
		self.Pre_Open_Interest = CLarge_Volume_Type() 
		#����ʵ��
		self.Pre_Delta = CRatio_Type() 
		#����
		self.Open_Price = CPrice_Type() 
		#��߼�
		self.Highest_Price = CPrice_Type() 
		#��ͼ�
		self.Lowest_Price = CPrice_Type() 
		#������
		self.Close_Price = CPrice_Type() 
		#��ͣ���
		self.Upper_Limit_Price = CPrice_Type() 
		#��ͣ���
		self.Lower_Limit_Price = CPrice_Type() 
		#�����
		self.Settlement_Price = CPrice_Type() 
		#����ʵ��
		self.Curr_Delta = CRatio_Type() 
		#��ʷ��߼�
		self.Life_Hight = CPrice_Type() 
		#��ʷ��ͼ�
		self.Life_Low = CPrice_Type() 
		#���¼�
		self.Last_Price = CPrice_Type() 
		#���³ɽ���
		self.Last_Match_Volume = CVolume_Type() 
		#�ɽ����
		self.Turnover = CMoney_Type() 
		#�ɽ���
		self.Total_Match_Volume = CVolume_Type() 
		#�ֲ���
		self.Open_Interest = CLarge_Volume_Type() 
		#�ֲ����仯
		self.Interest_Change = CVolume_Type() 
		#���վ���
		self.Average_Price = CPrice_Type() 
		#�����һ
		self.Bid_Price1 = CPrice_Type() 
		#������һ
		self.Bid_Volume1 = CVolume_Type() 
		#������һ
		self.Ask_Price1 = CPrice_Type() 
		#������һ
		self.Ask_Volume1 = CVolume_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 

#�ͻ��ֲ�Ӧ��
class CCustomer_Position_Field:
    def __init__(self):
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#1����2����
		self.Direction = CDirection_Type() 
		#�ֲֵĵ�ǰ����
		self.Position = CVolume_Type() 
		#�ֱֲ�֤��
		self.Margin = CMoney_Type() 
		#�ֲ־���
		self.Hold_Average_Price = CPrice_Type() 
		#���־���
		self.Open_Average_Price = CPrice_Type() 
		#���ճֲֵĵ�ǰ����
		self.Today_Position = CVolume_Type() 
		#�ܶ���
		self.Total_Frozen = CVolume_Type() 
		#���ն���
		self.Today_Frozen = CVolume_Type() 

#�����˻��ʽ���Ϣ
class CReal_Account_Field:
    def __init__(self):
		#�ڲ��ʽ��ʺŵı�ʶ
		self.Account_ID = CAccount_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#���ս��
		self.Last_Remain = CMoney_Type() 
		#�����
		self.Money_In_Out = CMoney_Type() 
		#����Total����Curr_Margin��Available_Collateral��
		self.Available = CMoney_Type() 
		#Available+����ӯ��
		self.Dyn_Rights = CMoney_Type() 
		#����Close_Profit + Position_Profit
		self.Profit = CMoney_Type() 
		#ƽ����ɵ�ӯ�����
		self.Close_Profit = CMoney_Type() 
		#�ֲ���ɵ�ӯ�����
		self.Position_Profit = CMoney_Type() 
		#�ڻ��ֲ�ռ�õı�֤��
		self.Margin = CMoney_Type() 
		#���ᱣ֤���ʽ�
		self.Forzen_Margin = CMoney_Type() 
		#�򶳽ᱣ֤��
		self.Buy_Margin_Frozen = CMoney_Type() 
		#�򶳽ᱣ֤��
		self.Sell_Margin_Frozen = CMoney_Type() 
		#���յ�����������֧��
		self.Fee = CMoney_Type() 
		#����������
		self.Frozen_Fee = CMoney_Type() 
		#�ܶ���
		self.Total_Frozen = CMoney_Type() 
		#����min��Total_Collateral��Curr_Margin��80����
		self.Collateral_For_Margin = CMoney_Type() 
		#�ʻ�״̬
		self.Account_Status = CAccount_Status_Type() 

#�ͻ���Լ�ֲ���ϸ
class CCustomer_Detail_Position_Field:
    def __init__(self):
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#1����2����
		self.Direction = CDirection_Type() 
		#�ֲֵĵ�ǰ����
		self.Position = CVolume_Type() 
		#�ֱֲ�֤��
		self.Margin = CMoney_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#�ɽ����
		self.Trade_ID = CTrade_ID_Type() 
		#�ֲּ۸�
		self.Hold_Price = CPrice_Type() 
		#���ּ۸�
		self.Open_Price = CPrice_Type() 
		#�ֲ���ɵ�ӯ�����
		self.Position_Profit = CMoney_Type() 

#�ͻ���Լ�ֲֻ���
class CCustomer_Total_Position_Field:
    def __init__(self):
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_Trade_Code = CCustomer_Trade_Code_Type() 
		#1����2����
		self.Direction = CDirection_Type() 
		#�ֲֵĵ�ǰ����
		self.Position = CVolume_Type() 
		#�ֱֲ�֤��
		self.Margin = CMoney_Type() 
		#�ֲ־���
		self.Hold_Average_Price = CPrice_Type() 
		#���־���
		self.Open_Average_Price = CPrice_Type() 
		#���ճֲֵĵ�ǰ����
		self.Today_Position = CVolume_Type() 
		#�ܶ���
		self.Total_Frozen = CVolume_Type() 
		#���ն���
		self.Today_Frozen = CVolume_Type() 

#���̻�ע��
class COffer_Regist_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#����Ա��ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Seat_ID = CSeat_ID_Type() 
		#һ�����̻��ı��
		self.Offer_ID = COffer_ID_Type() 
		#һ�����̻�������
		self.Offer_Name = COffer_Name_Type() 
		#���̻�״̬
		self.Offer_Status = COffer_Status_Type() 
		#���̻��ĻỰID
		self.Offer_SessionID = COffer_SessionID_Type() 

#�ͻ���ʼ��״̬
class CCustomer_Initial_Status_Field:
    def __init__(self):
		#�Ự��ʶ
		self.Session_ID = CSession_ID_Type() 
		#��ʼ��״̬
		self.Initial_Status = CInitial_Status_Type() 

#��Ϣ��ѯ
class CInformation_Field:
    def __init__(self):
		#���
		self.Information_ID = CInformation_ID_Type() 
		#���к�
		self.Sequence_No = CSequence_No_Type() 
		#��Ϣ��������
		self.Content = CContent_Type() 
		#���ĳ���
		self.Content_Length = CContent_Length_Type() 
		#�Ƿ����
		self.Is_Accomplished = CBool_Type() 

#���鶩��
class CSubscribeQuote_Field:
    def __init__(self):
		#����������
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 

#����������
class CTrigger_Action_Field:
    def __init__(self):
		#������־
		self.Action_Flag = CTrigger_Action_Flag_Type() 
		#����ʱ��
		self.Active_Time = CTime_Type() 
		#������ID
		self.Trigger_ID = CSequence_No_Type() 

#������־
class COperation_Log_Field:
    def __init__(self):
		#��ǰ����
		self.Operation_Date = CDate_Type() 
		#ʱ��
		self.Operation_Time = CTime_Type() 
		#�������к�
		self.Sequence_No = CSequence_No_Type() 
		#����Ա����
		self.Operator_ID = COperator_ID_Type() 
		#��������
		self.Operation_Type = COperation_Type_Type() 
		#����ժҪ
		self.Operation_Desc = CContent_Type() 
		#����ժҪ
		self.Operation_Result = CContent_Type() 

#������ʱ��
class CExchange_Time_Field:
    def __init__(self):
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#����������
		self.Exchange_Name = CExchange_Name_Type() 
		#�������к�
		self.Sequence_No = CSequence_No_Type() 
		#��ǰ���ڣ��꣩
		self.Curr_Year = CYear_Type() 
		#��ǰʱ�䣨�·ݣ�
		self.Curr_Month = CMonth_Type() 
		#��ǰʱ�䣨���ڣ�
		self.Curr_Day = CDay_Type() 
		#��ǰ���ڣ�Сʱ��
		self.Curr_Hour = CHour_Type() 
		#��ǰ���ڣ����ӣ�
		self.Curr_Minute = CMinute_Type() 
		#��ǰʱ�䣨�룩
		self.Curr_Second = CSecond_Type() 
		#��ǰʱ�䣨���룩
		self.Curr_Millisec = CMillisec_Type() 
		#���ʱ��
		self.Relative_Time = CSerial_No_Type() 

#������ѯ
class CQry_Order_Field:
    def __init__(self):
		#�������
		self.Order_Sys_ID = COrder_Sys_ID_Type() 
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 

#�ɽ���ѯ
class CQry_Trade_Field:
    def __init__(self):
		#��ʼ��Լ����
		self.Inst_ID_Start = CInstrument_ID_Type() 
		#������Լ����
		self.Inst_ID_End = CInstrument_ID_Type() 
		#�ɽ����
		self.Trade_ID = CTrade_ID_Type() 
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 

#�����ѯ
class CQry_Market_Data_Field:
    def __init__(self):
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 

#�ͻ��ֲֲ�ѯ
class CQry_Customer_Position_Field:
    def __init__(self):
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 
		#��ʼ��Լ����
		self.Inst_ID_Start = CInstrument_ID_Type() 
		#������Լ����
		self.Inst_ID_End = CInstrument_ID_Type() 

#�����ʽ��ѯ
class CQry_Account_Field:
    def __init__(self):
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 
		#�ʽ��ʺ�
		self.Account_ID = CAccount_ID_Type() 

#��Լ��ѯ
class CQry_Instrument_Field:
    def __init__(self):
		#����������
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 

#������״̬��ѯ
class CQry_Exchange_Status_Field:
    def __init__(self):
		#����������
		self.Exchange_ID = CExchange_ID_Type() 

#��Լ��λ��ѯ
class CQry_MBLMarket_Data_Field:
    def __init__(self):
		#����������
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 

#��ѯ�ͻ�
class CQry_Customer_Field:
    def __init__(self):
		#��ʼ�ͻ�����
		self.Customer_ID_Start = CCustomer_ID_Type() 
		#�����ͻ�����
		self.Customer_ID_End = CCustomer_ID_Type() 

#��ѯ�ͻ�Ӧ��
class CQry_Rsp_Customer_Field:
    def __init__(self):
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#�ͻ�����
		self.Customer_Name = CParty_Name_Type() 
		#��Ȼ�ˣ�����
		self.Customer_Type = CCustomer_Type_Type() 
		#����
		self.Password = CPassword_Type() 
		#�ͻ��˵ı���ID��ϵͳֻ�Ǽ�¼�����أ���������ֶ�
		self.Customer_Order_Local_ID = COrder_Local_ID_Type() 
		#������ֻ��ƽ�֣���ֹ����
		self.Customer_Status = CCustomer_Status_Type() 

#��Ϣ��ѯ
class CQry_Information_Field:
    def __init__(self):
		#��ʼ��Ϣ����
		self.Information_ID_Start = CInformation_ID_Type() 
		#������Ϣ����
		self.Information_ID_End = CInformation_ID_Type() 

#����������ѯ
class CQry_Trigger_Order_Field:
    def __init__(self):
		#����ָ������
		self.Order_Local_Instruction_Type = COrder_Local_Instruction_Type_Type() 
		#����ָ�����
		self.Order_Local_Instruction_ID = COrder_Local_Instruction_ID_Type() 
		#�ͻ�����
		self.Customer_ID = CCustomer_ID_Type() 

#��Լ����
class CCurr_Instrument_Property_Field:
    def __init__(self):
		#�г��۱���������µ���
		self.Max_Market_Order_Volume = CVolume_Type() 
		#�г��۱�������С�µ���
		self.Min_Market_Order_Volume = CVolume_Type() 
		#�޼۱���������µ���
		self.Max_Limit_Order_Volume = CVolume_Type() 
		#�޼۱�������С�µ���
		self.Min_Limit_Order_Volume = CVolume_Type() 
		#���ֲ���
		self.Max_Limit_Position_Volume = CVolume_Type() 
		#��Լ�ĵ�λ�۸��ǵ��仯����Сֵ
		self.Price_Tick = CPrice_Type() 

#��ǰ��Լ����
class CInstrument_Rate_Field:
    def __init__(self):
		#��֤����
		self.Margin_Rate = CRatio_Type() 
		#��������
		self.Fee_Rate = CRatio_Type() 
		#ƽ��������
		self.Offset_Today_Rate = CRatio_Type() 

#�г�����
class CMarket_Data_Field:
    def __init__(self):
		#���ոú�Լ�����ڼ�����³ɽ��۸�
		self.Last_Price = CPrice_Type() 
		#��һ�յĽ����
		self.Pre_Settlement_Price = CPrice_Type() 
		#��һ�����̼�
		self.Pre_Close_Price = CPrice_Type() 
		#ǰ���ֲ�����˫�����
		self.Pre_Open_Interest = CLarge_Volume_Type() 
		#���ڻ���Լ����ǰ������ھ����Ͼ��۲����ĳɽ��۸�
		self.Open_Price = CPrice_Type() 
		#ָһ��ʱ���ڸú�Լ�ɽ����е���߳ɽ��۸�
		self.Highest_Price = CPrice_Type() 
		#ָһ��ʱ���ڸú�Լ�ɽ����е���ͳɽ��۸�
		self.Lowest_Price = CPrice_Type() 
		#�ú�Լ�ڵ��ս����ڼ����гɽ���Լ��˫������
		self.Volume = CVolume_Type() 
		#�ú�Լ��ɽ��׵���ֵ
		self.Turnover = CMoney_Type() 
		#���ֲ�����˫�����
		self.Open_Interest = CLarge_Volume_Type() 
		#�ú�Լ���ս��׵����һ�ʳɽ��۸�
		self.Close_Price = CPrice_Type() 
		#�ú�Լ���ճɽ��۸񰴳ɽ����ļ�Ȩƽ���ۣ������޳ɽ��ģ�����һ�ս����
		self.Settlement_Price = CPrice_Type() 
		#��ͣ���
		self.Upper_Limit_Price = CPrice_Type() 
		#��ͣ���
		self.Lower_Limit_Price = CPrice_Type() 
		#����޸�ʱ��
		self.Update_Time = CTime_Type() 
		#����޸ĺ���
		self.Update_Millisec = CMillisec_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 

#�������
class CDepth_Market_Data_Field:
    def __init__(self):
		#���ոú�Լ�����ڼ�����³ɽ��۸�
		self.Last_Price = CPrice_Type() 
		#��һ�յĽ����
		self.Pre_Settlement_Price = CPrice_Type() 
		#��һ�����̼�
		self.Pre_Close_Price = CPrice_Type() 
		#ǰ���ֲ�����˫�����
		self.Pre_Open_Interest = CLarge_Volume_Type() 
		#���ڻ���Լ����ǰ������ھ����Ͼ��۲����ĳɽ��۸�
		self.Open_Price = CPrice_Type() 
		#ָһ��ʱ���ڸú�Լ�ɽ����е���߳ɽ��۸�
		self.Highest_Price = CPrice_Type() 
		#ָһ��ʱ���ڸú�Լ�ɽ����е���ͳɽ��۸�
		self.Lowest_Price = CPrice_Type() 
		#�ú�Լ�ڵ��ս����ڼ����гɽ���Լ��˫������
		self.Volume = CVolume_Type() 
		#�ú�Լ��ɽ��׵���ֵ
		self.Turnover = CMoney_Type() 
		#���ֲ�����˫�����
		self.Open_Interest = CLarge_Volume_Type() 
		#�ú�Լ���ս��׵����һ�ʳɽ��۸�
		self.Close_Price = CPrice_Type() 
		#�ú�Լ���ճɽ��۸񰴳ɽ����ļ�Ȩƽ���ۣ������޳ɽ��ģ�����һ�ս����
		self.Settlement_Price = CPrice_Type() 
		#��ͣ���
		self.Upper_Limit_Price = CPrice_Type() 
		#��ͣ���
		self.Lower_Limit_Price = CPrice_Type() 
		#����޸�ʱ��
		self.Update_Time = CTime_Type() 
		#����޸ĺ���
		self.Update_Millisec = CMillisec_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������߼�λ
		self.Bid_Price1 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����߼�λ����������µ���
		self.Bid_Volume1 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������ͼ�λ
		self.Ask_Price1 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����ͼ�λ�����������µ���
		self.Ask_Volume1 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������߼�λ
		self.Bid_Price2 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����߼�λ����������µ���
		self.Bid_Volume2 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������ͼ�λ
		self.Ask_Price2 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����ͼ�λ�����������µ���
		self.Ask_Volume2 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������߼�λ
		self.Bid_Price3 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����߼�λ����������µ���
		self.Bid_Volume3 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������ͼ�λ
		self.Ask_Price3 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����ͼ�λ�����������µ���
		self.Ask_Volume3 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������߼�λ
		self.Bid_Price4 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����߼�λ����������µ���
		self.Bid_Volume4 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������ͼ�λ
		self.Ask_Price4 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����ͼ�λ�����������µ���
		self.Ask_Volume4 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������߼�λ
		self.Bid_Price5 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����߼�λ����������µ���
		self.Bid_Volume5 = CVolume_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�������������ͼ�λ
		self.Ask_Price5 = CPrice_Type() 
		#�ú�Լ���ս���������ϵͳ��δ�ɽ�����ͼ�λ�����������µ���
		self.Ask_Volume5 = CVolume_Type() 

#�ּ۱�
class CMBL_Market_Data_Field:
    def __init__(self):
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 
		#��������
		self.Direction = CDirection_Type() 
		#�۸�
		self.Price = CPrice_Type() 
		#����
		self.Volume = CVolume_Type() 

#�����������
class CMarket_Data_Base_Field:
    def __init__(self):
		#������
		self.Trading_Day = CDate_Type() 
		#�����
		self.Pre_Settlement_Price = CPrice_Type() 
		#������
		self.Pre_Close_Price = CPrice_Type() 
		#��ֲ���
		self.Pre_Open_Interest = CLarge_Volume_Type() 
		#����ʵ��
		self.Pre_Delta = CRatio_Type() 

#���龲̬����
class CMarket_Data_Static_Field:
    def __init__(self):
		#����
		self.Open_Price = CPrice_Type() 
		#��߼�
		self.Highest_Price = CPrice_Type() 
		#��ͼ�
		self.Lowest_Price = CPrice_Type() 
		#������
		self.Close_Price = CPrice_Type() 
		#��ͣ���
		self.Upper_Limit_Price = CPrice_Type() 
		#��ͣ���
		self.Lower_Limit_Price = CPrice_Type() 
		#�����
		self.Settlement_Price = CPrice_Type() 
		#����ʵ��
		self.Curr_Delta = CRatio_Type() 
		#��ʷ��߼�
		self.Life_Hight = CPrice_Type() 
		#��ʷ��ͼ�
		self.Life_Low = CPrice_Type() 

#�������³ɽ�����
class CMarket_Data_Last_Match_Field:
    def __init__(self):
		#���¼�
		self.Last_Price = CPrice_Type() 
		#���³ɽ���
		self.Last_Match_Volume = CVolume_Type() 
		#�ɽ����
		self.Turnover = CMoney_Type() 
		#�ɽ���
		self.Total_Match_Volume = CVolume_Type() 
		#�ֲ���
		self.Open_Interest = CLarge_Volume_Type() 
		#�ֲ����仯
		self.Interest_Change = CVolume_Type() 
		#���վ���
		self.Average_Price = CPrice_Type() 

#�������ż�����
class CMarket_Data_Best_Price_Field:
    def __init__(self):
		#�����һ
		self.Bid_Price1 = CPrice_Type() 
		#������һ
		self.Bid_Volume1 = CVolume_Type() 
		#������һ
		self.Ask_Price1 = CPrice_Type() 
		#������һ
		self.Ask_Volume1 = CVolume_Type() 

#���������_������
class CMarket_Data_Bid23_Field:
    def __init__(self):
		#����۶�
		self.Bid_Price2 = CPrice_Type() 
		#��������
		self.Bid_Volume2 = CVolume_Type() 
		#�������
		self.Bid_Price3 = CPrice_Type() 
		#��������
		self.Bid_Volume3 = CVolume_Type() 

#����������_������
class CMarket_Data_Ask23_Field:
    def __init__(self):
		#�����۶�
		self.Ask_Price2 = CPrice_Type() 
		#��������
		self.Ask_Volume2 = CVolume_Type() 
		#��������
		self.Ask_Price3 = CPrice_Type() 
		#��������
		self.Ask_Volume3 = CVolume_Type() 

#����������_������
class CMarket_Data_Bid45_Field:
    def __init__(self):
		#�������
		self.Bid_Price4 = CPrice_Type() 
		#��������
		self.Bid_Volume4 = CVolume_Type() 
		#�������
		self.Bid_Price5 = CPrice_Type() 
		#��������
		self.Bid_Volume5 = CVolume_Type() 

#����������_������
class CMarket_Data_Ask45_Field:
    def __init__(self):
		#��������
		self.Ask_Price4 = CPrice_Type() 
		#��������
		self.Ask_Volume4 = CVolume_Type() 
		#��������
		self.Ask_Price5 = CPrice_Type() 
		#��������
		self.Ask_Volume5 = CVolume_Type() 

#�������ʱ������
class CMarket_Data_Update_Time_Field:
    def __init__(self):
		#��Լ����
		self.Instrument_ID = CInstrument_ID_Type() 
		#����޸�ʱ��
		self.Update_Time = CTime_Type() 
		#����޸ĺ���
		self.Update_Millisec = CMillisec_Type() 

#�ּ���
class CShort_MBL_Market_Data_Field:
    def __init__(self):
		#��������
		self.Direction = CDirection_Type() 
		#�۸�
		self.Price = CPrice_Type() 
		#����
		self.Volume = CVolume_Type() 

#�ͻ���Լ
class CCustomer_Instrument_Field:
    def __init__(self):
		#Ʒ����ϵͳ�еı��
		self.Variety_ID = CVariety_ID_Type() 
		#������Լ�ĳֲ�����
		self.Position_Type = CPosition_Type_Type() 
		#Ʒ�ֵ�ÿ�ֽ��׵Ĺ涨��������Ի�������Ʒ
		self.Volume_Multiple = CVolume_Multiple_Type() 
		#һ���������ı��
		self.Exchange_ID = CExchange_ID_Type() 
		#��Լ��ϵͳ�еı��
		self.Instrument_ID = CInstrument_ID_Type() 
		#��Լ������
		self.Instrument_Name = CInstrument_Name_Type() 
		#�ú�Լ�涨����ʵ�ｻ������
		self.Delivery_Year = CYear_Type() 
		#�ú�Լ�涨����ʵ�ｻ����·�
		self.Delivery_Month = CMonth_Type() 
		#�г��۱���������µ���
		self.Max_Market_Order_Volume = CVolume_Type() 
		#�г��۱�������С�µ���
		self.Min_Market_Order_Volume = CVolume_Type() 
		#�޼۱���������µ���
		self.Max_Limit_Order_Volume = CVolume_Type() 
		#�޼۱�������С�µ���
		self.Min_Limit_Order_Volume = CVolume_Type() 
		#���ֲ���
		self.Max_Limit_Position_Volume = CVolume_Type() 
		#��Լ�ĵ�λ�۸��ǵ��仯����Сֵ
		self.Price_Tick = CPrice_Type() 
		#��֤����
		self.Margin_Rate = CRatio_Type() 
		#��������
		self.Fee_Rate = CRatio_Type() 
		#ƽ��������
		self.Offset_Today_Rate = CRatio_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 

#�ͻ������
class CCustomer_IO_Money_Field:
    def __init__(self):
		#�������ˮ��
		self.Money_IO_Sequence_No = CSequence_String_Type() 
		#�ͻ���ϵͳ�еı�ţ����Ψһ����ѭ�������ƶ��ı������
		self.Customer_ID = CCustomer_ID_Type() 
		#��̨�յ����ĵ�����
		self.Receive_Date = CDate_Type() 
		#��̨�յ����ĵ�ʱ��
		self.Receive_Time = CTime_Type() 
		#���
		self.Money_In = CMoney_Type() 
		#����
		self.Money_Out = CMoney_Type() 
		#��ע
		self.Comment = CContent_Type() 
		#�ϳ�״̬
		self.Status = CMoney_IO_Up_Status_Type() 

