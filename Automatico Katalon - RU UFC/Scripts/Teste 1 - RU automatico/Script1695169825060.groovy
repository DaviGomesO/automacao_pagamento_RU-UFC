import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('https://si3.ufc.br/public//jsp/restaurante_universitario/consulta_comensal_ru.jsf')

WebUI.setText(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Nmero do carto_formj_id_jsp_1091681061_2'), 
    '2888854167')

WebUI.setText(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Matrcula atrelada ao carto_formj_id_j_2c591d'), 
    '511274')

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Campos de preenchimento obrigatrio_fo_328bc9'))

WebUI.doubleClick(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Quantidade de Crditos_formqtdCreditos'))

WebUI.setText(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Quantidade de Crditos_formqtdCreditos'), 
    '5')

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_Total a Pagar (R)_formj_id_jsp_540432864_5'))

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_GRU_formbtPagTesouro'))

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/input_ATENO_modalForm2btConfirmarPagtesouro'))

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/em_Formas de Pagamento_icone-meio-pagamento img-icone-pix'))

WebUI.click(findTestObject('Object Repository/Page_SIPAC - Sistema Integrado de Patrimnio_f8a443/a_Pagar'))

