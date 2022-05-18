# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtQml, except for defaults which are replaced by "...".
"""

# Module PySide2.QtQml
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtNetwork
import PySide2.QtQml


class ListProperty(PySide2.QtCore.Property):

    @staticmethod
    def __init__(type:type, append:typing.Callable, at:typing.Optional[typing.Callable]=..., clear:typing.Optional[typing.Callable]=..., count:typing.Optional[typing.Callable]=...) -> None: ...


class QJSEngine(PySide2.QtCore.QObject):
    AllExtensions            : QJSEngine = ... # -0x1
    TranslationExtension     : QJSEngine = ... # 0x1
    ConsoleExtension         : QJSEngine = ... # 0x2
    GarbageCollectionExtension: QJSEngine = ... # 0x4

    class Extension(object):
        AllExtensions            : QJSEngine.Extension = ... # -0x1
        TranslationExtension     : QJSEngine.Extension = ... # 0x1
        ConsoleExtension         : QJSEngine.Extension = ... # 0x2
        GarbageCollectionExtension: QJSEngine.Extension = ... # 0x4

    class Extensions(object): ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent:PySide2.QtCore.QObject) -> None: ...

    def collectGarbage(self) -> None: ...
    def evaluate(self, program:str, fileName:str=..., lineNumber:int=...) -> PySide2.QtQml.QJSValue: ...
    def globalObject(self) -> PySide2.QtQml.QJSValue: ...
    def importModule(self, fileName:str) -> PySide2.QtQml.QJSValue: ...
    def installExtensions(self, extensions:PySide2.QtQml.QJSEngine.Extensions, object:PySide2.QtQml.QJSValue=...) -> None: ...
    def installTranslatorFunctions(self, object:PySide2.QtQml.QJSValue=...) -> None: ...
    def isInterrupted(self) -> bool: ...
    def newArray(self, length:int=...) -> PySide2.QtQml.QJSValue: ...
    def newErrorObject(self, errorType:PySide2.QtQml.QJSValue.ErrorType, message:str=...) -> PySide2.QtQml.QJSValue: ...
    def newObject(self) -> PySide2.QtQml.QJSValue: ...
    def newQMetaObject(self, metaObject:PySide2.QtCore.QMetaObject) -> PySide2.QtQml.QJSValue: ...
    def newQObject(self, object:PySide2.QtCore.QObject) -> PySide2.QtQml.QJSValue: ...
    def setInterrupted(self, interrupted:bool) -> None: ...
    def setUiLanguage(self, language:str) -> None: ...
    @typing.overload
    def throwError(self, errorType:PySide2.QtQml.QJSValue.ErrorType, message:str=...) -> None: ...
    @typing.overload
    def throwError(self, message:str) -> None: ...
    def toScriptValue(self, arg__1:typing.Any) -> PySide2.QtQml.QJSValue: ...
    def uiLanguage(self) -> str: ...


class QJSValue(Shiboken.Object):
    NoError                  : QJSValue = ... # 0x0
    NullValue                : QJSValue = ... # 0x0
    GenericError             : QJSValue = ... # 0x1
    UndefinedValue           : QJSValue = ... # 0x1
    EvalError                : QJSValue = ... # 0x2
    RangeError               : QJSValue = ... # 0x3
    ReferenceError           : QJSValue = ... # 0x4
    SyntaxError              : QJSValue = ... # 0x5
    TypeError                : QJSValue = ... # 0x6
    URIError                 : QJSValue = ... # 0x7

    class ErrorType(object):
        NoError                  : QJSValue.ErrorType = ... # 0x0
        GenericError             : QJSValue.ErrorType = ... # 0x1
        EvalError                : QJSValue.ErrorType = ... # 0x2
        RangeError               : QJSValue.ErrorType = ... # 0x3
        ReferenceError           : QJSValue.ErrorType = ... # 0x4
        SyntaxError              : QJSValue.ErrorType = ... # 0x5
        TypeError                : QJSValue.ErrorType = ... # 0x6
        URIError                 : QJSValue.ErrorType = ... # 0x7

    class SpecialValue(object):
        NullValue                : QJSValue.SpecialValue = ... # 0x0
        UndefinedValue           : QJSValue.SpecialValue = ... # 0x1

    @typing.overload
    def __init__(self, other:PySide2.QtQml.QJSValue) -> None: ...
    @typing.overload
    def __init__(self, str:bytes) -> None: ...
    @typing.overload
    def __init__(self, value:PySide2.QtQml.QJSValue.SpecialValue=...) -> None: ...
    @typing.overload
    def __init__(self, value:str) -> None: ...
    @typing.overload
    def __init__(self, value:bool) -> None: ...
    @typing.overload
    def __init__(self, value:float) -> None: ...
    @typing.overload
    def __init__(self, value:int) -> None: ...
    @typing.overload
    def __init__(self, value:int) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def call(self, args:typing.Sequence=...) -> PySide2.QtQml.QJSValue: ...
    def callAsConstructor(self, args:typing.Sequence=...) -> PySide2.QtQml.QJSValue: ...
    def callWithInstance(self, instance:PySide2.QtQml.QJSValue, args:typing.Sequence=...) -> PySide2.QtQml.QJSValue: ...
    def deleteProperty(self, name:str) -> bool: ...
    def engine(self) -> PySide2.QtQml.QJSEngine: ...
    def equals(self, other:PySide2.QtQml.QJSValue) -> bool: ...
    def errorType(self) -> PySide2.QtQml.QJSValue.ErrorType: ...
    def hasOwnProperty(self, name:str) -> bool: ...
    def hasProperty(self, name:str) -> bool: ...
    def isArray(self) -> bool: ...
    def isBool(self) -> bool: ...
    def isCallable(self) -> bool: ...
    def isDate(self) -> bool: ...
    def isError(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isNumber(self) -> bool: ...
    def isObject(self) -> bool: ...
    def isQMetaObject(self) -> bool: ...
    def isQObject(self) -> bool: ...
    def isRegExp(self) -> bool: ...
    def isString(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def isVariant(self) -> bool: ...
    @typing.overload
    def property(self, arrayIndex:int) -> PySide2.QtQml.QJSValue: ...
    @typing.overload
    def property(self, name:str) -> PySide2.QtQml.QJSValue: ...
    def prototype(self) -> PySide2.QtQml.QJSValue: ...
    @typing.overload
    def setProperty(self, arrayIndex:int, value:PySide2.QtQml.QJSValue) -> None: ...
    @typing.overload
    def setProperty(self, name:str, value:PySide2.QtQml.QJSValue) -> None: ...
    def setPrototype(self, prototype:PySide2.QtQml.QJSValue) -> None: ...
    def strictlyEquals(self, other:PySide2.QtQml.QJSValue) -> bool: ...
    def toBool(self) -> bool: ...
    def toDateTime(self) -> PySide2.QtCore.QDateTime: ...
    def toInt(self) -> int: ...
    def toNumber(self) -> float: ...
    def toQMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def toQObject(self) -> PySide2.QtCore.QObject: ...
    def toString(self) -> str: ...
    def toUInt(self) -> int: ...
    def toVariant(self) -> typing.Any: ...


class QJSValueIterator(Shiboken.Object):

    def __init__(self, value:PySide2.QtQml.QJSValue) -> None: ...

    def hasNext(self) -> bool: ...
    def name(self) -> str: ...
    def next(self) -> bool: ...
    def value(self) -> PySide2.QtQml.QJSValue: ...


class QQmlAbstractUrlInterceptor(Shiboken.Object):
    QmlFile                  : QQmlAbstractUrlInterceptor = ... # 0x0
    JavaScriptFile           : QQmlAbstractUrlInterceptor = ... # 0x1
    QmldirFile               : QQmlAbstractUrlInterceptor = ... # 0x2
    UrlString                : QQmlAbstractUrlInterceptor = ... # 0x1000

    class DataType(object):
        QmlFile                  : QQmlAbstractUrlInterceptor.DataType = ... # 0x0
        JavaScriptFile           : QQmlAbstractUrlInterceptor.DataType = ... # 0x1
        QmldirFile               : QQmlAbstractUrlInterceptor.DataType = ... # 0x2
        UrlString                : QQmlAbstractUrlInterceptor.DataType = ... # 0x1000

    def __init__(self) -> None: ...

    def intercept(self, path:PySide2.QtCore.QUrl, type:PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType) -> PySide2.QtCore.QUrl: ...


class QQmlApplicationEngine(PySide2.QtQml.QQmlEngine):

    @typing.overload
    def __init__(self, filePath:str, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, url:PySide2.QtCore.QUrl, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    @typing.overload
    def load(self, filePath:str) -> None: ...
    @typing.overload
    def load(self, url:PySide2.QtCore.QUrl) -> None: ...
    def loadData(self, data:PySide2.QtCore.QByteArray, url:PySide2.QtCore.QUrl=...) -> None: ...
    def rootObjects(self) -> typing.List: ...
    def setInitialProperties(self, initialProperties:typing.Dict) -> None: ...


class QQmlComponent(PySide2.QtCore.QObject):
    Null                     : QQmlComponent = ... # 0x0
    PreferSynchronous        : QQmlComponent = ... # 0x0
    Asynchronous             : QQmlComponent = ... # 0x1
    Ready                    : QQmlComponent = ... # 0x1
    Loading                  : QQmlComponent = ... # 0x2
    Error                    : QQmlComponent = ... # 0x3

    class CompilationMode(object):
        PreferSynchronous        : QQmlComponent.CompilationMode = ... # 0x0
        Asynchronous             : QQmlComponent.CompilationMode = ... # 0x1

    class Status(object):
        Null                     : QQmlComponent.Status = ... # 0x0
        Ready                    : QQmlComponent.Status = ... # 0x1
        Loading                  : QQmlComponent.Status = ... # 0x2
        Error                    : QQmlComponent.Status = ... # 0x3

    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, fileName:str, mode:PySide2.QtQml.QQmlComponent.CompilationMode, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, fileName:str, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, url:PySide2.QtCore.QUrl, mode:PySide2.QtQml.QQmlComponent.CompilationMode, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, url:PySide2.QtCore.QUrl, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def beginCreate(self, arg__1:PySide2.QtQml.QQmlContext) -> PySide2.QtCore.QObject: ...
    def completeCreate(self) -> None: ...
    @typing.overload
    def create(self, arg__1:PySide2.QtQml.QQmlIncubator, context:typing.Optional[PySide2.QtQml.QQmlContext]=..., forContext:typing.Optional[PySide2.QtQml.QQmlContext]=...) -> None: ...
    @typing.overload
    def create(self, context:typing.Optional[PySide2.QtQml.QQmlContext]=...) -> PySide2.QtCore.QObject: ...
    def createWithInitialProperties(self, initialProperties:typing.Dict, context:typing.Optional[PySide2.QtQml.QQmlContext]=...) -> PySide2.QtCore.QObject: ...
    def creationContext(self) -> PySide2.QtQml.QQmlContext: ...
    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def errorString(self) -> str: ...
    def errors(self) -> typing.List: ...
    def isError(self) -> bool: ...
    def isLoading(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isReady(self) -> bool: ...
    @typing.overload
    def loadUrl(self, url:PySide2.QtCore.QUrl) -> None: ...
    @typing.overload
    def loadUrl(self, url:PySide2.QtCore.QUrl, mode:PySide2.QtQml.QQmlComponent.CompilationMode) -> None: ...
    def progress(self) -> float: ...
    def setData(self, arg__1:PySide2.QtCore.QByteArray, baseUrl:PySide2.QtCore.QUrl) -> None: ...
    def setInitialProperties(self, component:PySide2.QtCore.QObject, properties:typing.Dict) -> None: ...
    def status(self) -> PySide2.QtQml.QQmlComponent.Status: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QQmlContext(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self, parent:PySide2.QtQml.QQmlContext, objParent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, parent:PySide2.QtQml.QQmlEngine, objParent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def baseUrl(self) -> PySide2.QtCore.QUrl: ...
    def contextObject(self) -> PySide2.QtCore.QObject: ...
    def contextProperty(self, arg__1:str) -> typing.Any: ...
    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def isValid(self) -> bool: ...
    def nameForObject(self, arg__1:PySide2.QtCore.QObject) -> str: ...
    def parentContext(self) -> PySide2.QtQml.QQmlContext: ...
    def resolvedUrl(self, arg__1:PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl: ...
    def setBaseUrl(self, arg__1:PySide2.QtCore.QUrl) -> None: ...
    def setContextObject(self, arg__1:PySide2.QtCore.QObject) -> None: ...
    @typing.overload
    def setContextProperty(self, arg__1:str, arg__2:PySide2.QtCore.QObject) -> None: ...
    @typing.overload
    def setContextProperty(self, arg__1:str, arg__2:typing.Any) -> None: ...


class QQmlDebuggingEnabler(Shiboken.Object):
    DoNotWaitForClient       : QQmlDebuggingEnabler = ... # 0x0
    WaitForClient            : QQmlDebuggingEnabler = ... # 0x1

    class StartMode(object):
        DoNotWaitForClient       : QQmlDebuggingEnabler.StartMode = ... # 0x0
        WaitForClient            : QQmlDebuggingEnabler.StartMode = ... # 0x1

    def __init__(self, printWarning:bool=...) -> None: ...

    @staticmethod
    def connectToLocalDebugger(socketFileName:str, mode:PySide2.QtQml.QQmlDebuggingEnabler.StartMode=...) -> bool: ...
    @staticmethod
    def debuggerServices() -> typing.List: ...
    @staticmethod
    def inspectorServices() -> typing.List: ...
    @staticmethod
    def nativeDebuggerServices() -> typing.List: ...
    @staticmethod
    def profilerServices() -> typing.List: ...
    @staticmethod
    def setServices(services:typing.Sequence) -> None: ...
    @staticmethod
    def startDebugConnector(pluginName:str, configuration:typing.Dict=...) -> bool: ...
    @staticmethod
    def startTcpDebugServer(port:int, mode:PySide2.QtQml.QQmlDebuggingEnabler.StartMode=..., hostName:str=...) -> bool: ...


class QQmlEngine(PySide2.QtQml.QJSEngine):
    CppOwnership             : QQmlEngine = ... # 0x0
    JavaScriptOwnership      : QQmlEngine = ... # 0x1

    class ObjectOwnership(object):
        CppOwnership             : QQmlEngine.ObjectOwnership = ... # 0x0
        JavaScriptOwnership      : QQmlEngine.ObjectOwnership = ... # 0x1

    def __init__(self, p:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def addImageProvider(self, id:str, arg__2:PySide2.QtQml.QQmlImageProviderBase) -> None: ...
    def addImportPath(self, dir:str) -> None: ...
    def addNamedBundle(self, name:str, fileName:str) -> bool: ...
    def addPluginPath(self, dir:str) -> None: ...
    def baseUrl(self) -> PySide2.QtCore.QUrl: ...
    def clearComponentCache(self) -> None: ...
    @staticmethod
    def contextForObject(arg__1:PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlContext: ...
    def event(self, arg__1:PySide2.QtCore.QEvent) -> bool: ...
    def imageProvider(self, id:str) -> PySide2.QtQml.QQmlImageProviderBase: ...
    def importPathList(self) -> typing.List: ...
    def importPlugin(self, filePath:str, uri:str, errors:typing.Sequence) -> bool: ...
    def incubationController(self) -> PySide2.QtQml.QQmlIncubationController: ...
    def networkAccessManager(self) -> PySide2.QtNetwork.QNetworkAccessManager: ...
    def networkAccessManagerFactory(self) -> PySide2.QtQml.QQmlNetworkAccessManagerFactory: ...
    @staticmethod
    def objectOwnership(arg__1:PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlEngine.ObjectOwnership: ...
    def offlineStorageDatabaseFilePath(self, databaseName:str) -> str: ...
    def offlineStoragePath(self) -> str: ...
    def outputWarningsToStandardError(self) -> bool: ...
    def pluginPathList(self) -> typing.List: ...
    def removeImageProvider(self, id:str) -> None: ...
    def retranslate(self) -> None: ...
    def rootContext(self) -> PySide2.QtQml.QQmlContext: ...
    def setBaseUrl(self, arg__1:PySide2.QtCore.QUrl) -> None: ...
    @staticmethod
    def setContextForObject(arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtQml.QQmlContext) -> None: ...
    def setImportPathList(self, paths:typing.Sequence) -> None: ...
    def setIncubationController(self, arg__1:PySide2.QtQml.QQmlIncubationController) -> None: ...
    def setNetworkAccessManagerFactory(self, arg__1:PySide2.QtQml.QQmlNetworkAccessManagerFactory) -> None: ...
    @staticmethod
    def setObjectOwnership(arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtQml.QQmlEngine.ObjectOwnership) -> None: ...
    def setOfflineStoragePath(self, dir:str) -> None: ...
    def setOutputWarningsToStandardError(self, arg__1:bool) -> None: ...
    def setPluginPathList(self, paths:typing.Sequence) -> None: ...
    def setUrlInterceptor(self, urlInterceptor:PySide2.QtQml.QQmlAbstractUrlInterceptor) -> None: ...
    def trimComponentCache(self) -> None: ...
    def urlInterceptor(self) -> PySide2.QtQml.QQmlAbstractUrlInterceptor: ...


class QQmlError(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlError) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def column(self) -> int: ...
    def description(self) -> str: ...
    def isValid(self) -> bool: ...
    def line(self) -> int: ...
    def messageType(self) -> PySide2.QtCore.QtMsgType: ...
    def object(self) -> PySide2.QtCore.QObject: ...
    def setColumn(self, arg__1:int) -> None: ...
    def setDescription(self, arg__1:str) -> None: ...
    def setLine(self, arg__1:int) -> None: ...
    def setMessageType(self, messageType:PySide2.QtCore.QtMsgType) -> None: ...
    def setObject(self, arg__1:PySide2.QtCore.QObject) -> None: ...
    def setUrl(self, arg__1:PySide2.QtCore.QUrl) -> None: ...
    def toString(self) -> str: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QQmlExpression(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlContext, arg__2:PySide2.QtCore.QObject, arg__3:str, arg__4:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlScriptString, arg__2:typing.Optional[PySide2.QtQml.QQmlContext]=..., arg__3:typing.Optional[PySide2.QtCore.QObject]=..., arg__4:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def clearError(self) -> None: ...
    def columnNumber(self) -> int: ...
    def context(self) -> PySide2.QtQml.QQmlContext: ...
    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def error(self) -> PySide2.QtQml.QQmlError: ...
    def evaluate(self) -> typing.Tuple: ...
    def expression(self) -> str: ...
    def hasError(self) -> bool: ...
    def lineNumber(self) -> int: ...
    def notifyOnValueChanged(self) -> bool: ...
    def scopeObject(self) -> PySide2.QtCore.QObject: ...
    def setExpression(self, arg__1:str) -> None: ...
    def setNotifyOnValueChanged(self, arg__1:bool) -> None: ...
    def setSourceLocation(self, fileName:str, line:int, column:int=...) -> None: ...
    def sourceFile(self) -> str: ...


class QQmlExtensionInterface(PySide2.QtQml.QQmlTypesExtensionInterface):

    def __init__(self) -> None: ...

    def initializeEngine(self, engine:PySide2.QtQml.QQmlEngine, uri:bytes) -> None: ...


class QQmlExtensionPlugin(PySide2.QtCore.QObject, PySide2.QtQml.QQmlExtensionInterface):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def baseUrl(self) -> PySide2.QtCore.QUrl: ...
    def initializeEngine(self, engine:PySide2.QtQml.QQmlEngine, uri:bytes) -> None: ...
    def registerTypes(self, uri:bytes) -> None: ...


class QQmlFile(Shiboken.Object):
    Null                     : QQmlFile = ... # 0x0
    Ready                    : QQmlFile = ... # 0x1
    Error                    : QQmlFile = ... # 0x2
    Loading                  : QQmlFile = ... # 0x3

    class Status(object):
        Null                     : QQmlFile.Status = ... # 0x0
        Ready                    : QQmlFile.Status = ... # 0x1
        Error                    : QQmlFile.Status = ... # 0x2
        Loading                  : QQmlFile.Status = ... # 0x3

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, arg__2:PySide2.QtCore.QUrl) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlEngine, arg__2:str) -> None: ...

    @typing.overload
    def clear(self) -> None: ...
    @typing.overload
    def clear(self, arg__1:PySide2.QtCore.QObject) -> None: ...
    @typing.overload
    def connectDownloadProgress(self, arg__1:PySide2.QtCore.QObject, arg__2:bytes) -> bool: ...
    @typing.overload
    def connectDownloadProgress(self, arg__1:PySide2.QtCore.QObject, arg__2:int) -> bool: ...
    @typing.overload
    def connectFinished(self, arg__1:PySide2.QtCore.QObject, arg__2:bytes) -> bool: ...
    @typing.overload
    def connectFinished(self, arg__1:PySide2.QtCore.QObject, arg__2:int) -> bool: ...
    def data(self) -> bytes: ...
    def dataByteArray(self) -> PySide2.QtCore.QByteArray: ...
    def error(self) -> str: ...
    def isError(self) -> bool: ...
    def isLoading(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isLocalFile(url:PySide2.QtCore.QUrl) -> bool: ...
    @typing.overload
    @staticmethod
    def isLocalFile(url:str) -> bool: ...
    def isNull(self) -> bool: ...
    def isReady(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isSynchronous(url:PySide2.QtCore.QUrl) -> bool: ...
    @typing.overload
    @staticmethod
    def isSynchronous(url:str) -> bool: ...
    @typing.overload
    def load(self, arg__1:PySide2.QtQml.QQmlEngine, arg__2:PySide2.QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, arg__1:PySide2.QtQml.QQmlEngine, arg__2:str) -> None: ...
    def size(self) -> int: ...
    def status(self) -> PySide2.QtQml.QQmlFile.Status: ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    @staticmethod
    def urlToLocalFileOrQrc(arg__1:PySide2.QtCore.QUrl) -> str: ...
    @typing.overload
    @staticmethod
    def urlToLocalFileOrQrc(arg__1:str) -> str: ...


class QQmlFileSelector(PySide2.QtCore.QObject):

    def __init__(self, engine:PySide2.QtQml.QQmlEngine, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    @staticmethod
    def get(arg__1:PySide2.QtQml.QQmlEngine) -> PySide2.QtQml.QQmlFileSelector: ...
    def selector(self) -> PySide2.QtCore.QFileSelector: ...
    def setExtraSelectors(self, strings:typing.Sequence) -> None: ...
    def setSelector(self, selector:PySide2.QtCore.QFileSelector) -> None: ...


class QQmlImageProviderBase(Shiboken.Object):
    Image                    : QQmlImageProviderBase = ... # 0x0
    ForceAsynchronousImageLoading: QQmlImageProviderBase = ... # 0x1
    Pixmap                   : QQmlImageProviderBase = ... # 0x1
    Texture                  : QQmlImageProviderBase = ... # 0x2
    Invalid                  : QQmlImageProviderBase = ... # 0x3
    ImageResponse            : QQmlImageProviderBase = ... # 0x4

    class Flag(object):
        ForceAsynchronousImageLoading: QQmlImageProviderBase.Flag = ... # 0x1

    class Flags(object): ...

    class ImageType(object):
        Image                    : QQmlImageProviderBase.ImageType = ... # 0x0
        Pixmap                   : QQmlImageProviderBase.ImageType = ... # 0x1
        Texture                  : QQmlImageProviderBase.ImageType = ... # 0x2
        Invalid                  : QQmlImageProviderBase.ImageType = ... # 0x3
        ImageResponse            : QQmlImageProviderBase.ImageType = ... # 0x4
    def flags(self) -> PySide2.QtQml.QQmlImageProviderBase.Flags: ...
    def imageType(self) -> PySide2.QtQml.QQmlImageProviderBase.ImageType: ...


class QQmlIncubationController(Shiboken.Object):

    def __init__(self) -> None: ...

    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def incubateFor(self, msecs:int) -> None: ...
    def incubateWhile(self, msecs:int=...) -> bool: ...
    def incubatingObjectCount(self) -> int: ...
    def incubatingObjectCountChanged(self, arg__1:int) -> None: ...


class QQmlIncubator(Shiboken.Object):
    Asynchronous             : QQmlIncubator = ... # 0x0
    Null                     : QQmlIncubator = ... # 0x0
    AsynchronousIfNested     : QQmlIncubator = ... # 0x1
    Ready                    : QQmlIncubator = ... # 0x1
    Loading                  : QQmlIncubator = ... # 0x2
    Synchronous              : QQmlIncubator = ... # 0x2
    Error                    : QQmlIncubator = ... # 0x3

    class IncubationMode(object):
        Asynchronous             : QQmlIncubator.IncubationMode = ... # 0x0
        AsynchronousIfNested     : QQmlIncubator.IncubationMode = ... # 0x1
        Synchronous              : QQmlIncubator.IncubationMode = ... # 0x2

    class Status(object):
        Null                     : QQmlIncubator.Status = ... # 0x0
        Ready                    : QQmlIncubator.Status = ... # 0x1
        Loading                  : QQmlIncubator.Status = ... # 0x2
        Error                    : QQmlIncubator.Status = ... # 0x3

    def __init__(self, arg__1:PySide2.QtQml.QQmlIncubator.IncubationMode=...) -> None: ...

    def clear(self) -> None: ...
    def errors(self) -> typing.List: ...
    def forceCompletion(self) -> None: ...
    def incubationMode(self) -> PySide2.QtQml.QQmlIncubator.IncubationMode: ...
    def isError(self) -> bool: ...
    def isLoading(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isReady(self) -> bool: ...
    def object(self) -> PySide2.QtCore.QObject: ...
    def setInitialProperties(self, initialProperties:typing.Dict) -> None: ...
    def setInitialState(self, arg__1:PySide2.QtCore.QObject) -> None: ...
    def status(self) -> PySide2.QtQml.QQmlIncubator.Status: ...
    def statusChanged(self, arg__1:PySide2.QtQml.QQmlIncubator.Status) -> None: ...


class QQmlListReference(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, property:bytes, arg__3:typing.Optional[PySide2.QtQml.QQmlEngine]=...) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlListReference) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def append(self, arg__1:PySide2.QtCore.QObject) -> bool: ...
    def at(self, arg__1:int) -> PySide2.QtCore.QObject: ...
    def canAppend(self) -> bool: ...
    def canAt(self) -> bool: ...
    def canClear(self) -> bool: ...
    def canCount(self) -> bool: ...
    def canRemoveLast(self) -> bool: ...
    def canReplace(self) -> bool: ...
    def clear(self) -> bool: ...
    def count(self) -> int: ...
    def isManipulable(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def listElementType(self) -> PySide2.QtCore.QMetaObject: ...
    def object(self) -> PySide2.QtCore.QObject: ...
    def removeLast(self) -> bool: ...
    def replace(self, arg__1:int, arg__2:PySide2.QtCore.QObject) -> bool: ...


class QQmlNetworkAccessManagerFactory(Shiboken.Object):

    def __init__(self) -> None: ...

    def create(self, parent:PySide2.QtCore.QObject) -> PySide2.QtNetwork.QNetworkAccessManager: ...


class QQmlParserStatus(Shiboken.Object):

    def __init__(self) -> None: ...

    def classBegin(self) -> None: ...
    def componentComplete(self) -> None: ...


class QQmlProperty(Shiboken.Object):
    Invalid                  : QQmlProperty = ... # 0x0
    InvalidCategory          : QQmlProperty = ... # 0x0
    List                     : QQmlProperty = ... # 0x1
    Property                 : QQmlProperty = ... # 0x1
    Object                   : QQmlProperty = ... # 0x2
    SignalProperty           : QQmlProperty = ... # 0x2
    Normal                   : QQmlProperty = ... # 0x3

    class PropertyTypeCategory(object):
        InvalidCategory          : QQmlProperty.PropertyTypeCategory = ... # 0x0
        List                     : QQmlProperty.PropertyTypeCategory = ... # 0x1
        Object                   : QQmlProperty.PropertyTypeCategory = ... # 0x2
        Normal                   : QQmlProperty.PropertyTypeCategory = ... # 0x3

    class Type(object):
        Invalid                  : QQmlProperty.Type = ... # 0x0
        Property                 : QQmlProperty.Type = ... # 0x1
        SignalProperty           : QQmlProperty.Type = ... # 0x2

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtQml.QQmlContext) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtQml.QQmlEngine) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, arg__2:str) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:PySide2.QtQml.QQmlContext) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:PySide2.QtQml.QQmlEngine) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlProperty) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @typing.overload
    def connectNotifySignal(self, dest:PySide2.QtCore.QObject, method:int) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, dest:PySide2.QtCore.QObject, slot:bytes) -> bool: ...
    def hasNotifySignal(self) -> bool: ...
    def index(self) -> int: ...
    def isDesignable(self) -> bool: ...
    def isProperty(self) -> bool: ...
    def isResettable(self) -> bool: ...
    def isSignalProperty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def method(self) -> PySide2.QtCore.QMetaMethod: ...
    def name(self) -> str: ...
    def needsNotifySignal(self) -> bool: ...
    def object(self) -> PySide2.QtCore.QObject: ...
    def property(self) -> PySide2.QtCore.QMetaProperty: ...
    def propertyType(self) -> int: ...
    def propertyTypeCategory(self) -> PySide2.QtQml.QQmlProperty.PropertyTypeCategory: ...
    def propertyTypeName(self) -> bytes: ...
    @typing.overload
    @staticmethod
    def read(arg__1:PySide2.QtCore.QObject, arg__2:str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:PySide2.QtQml.QQmlContext) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:PySide2.QtQml.QQmlEngine) -> typing.Any: ...
    @typing.overload
    def read(self) -> typing.Any: ...
    def reset(self) -> bool: ...
    def type(self) -> PySide2.QtQml.QQmlProperty.Type: ...
    @typing.overload
    @staticmethod
    def write(arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def write(arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:typing.Any, arg__4:PySide2.QtQml.QQmlContext) -> bool: ...
    @typing.overload
    @staticmethod
    def write(arg__1:PySide2.QtCore.QObject, arg__2:str, arg__3:typing.Any, arg__4:PySide2.QtQml.QQmlEngine) -> bool: ...
    @typing.overload
    def write(self, arg__1:typing.Any) -> bool: ...


class QQmlPropertyMap(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def clear(self, key:str) -> None: ...
    def contains(self, key:str) -> bool: ...
    def count(self) -> int: ...
    def insert(self, key:str, value:typing.Any) -> None: ...
    def isEmpty(self) -> bool: ...
    def keys(self) -> typing.List: ...
    def size(self) -> int: ...
    def updateValue(self, key:str, input:typing.Any) -> typing.Any: ...
    def value(self, key:str) -> typing.Any: ...


class QQmlPropertyValueSource(Shiboken.Object):

    def __init__(self) -> None: ...

    def setTarget(self, arg__1:PySide2.QtQml.QQmlProperty) -> None: ...


class QQmlScriptString(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtQml.QQmlScriptString) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def booleanLiteral(self) -> typing.Tuple: ...
    def isEmpty(self) -> bool: ...
    def isNullLiteral(self) -> bool: ...
    def isUndefinedLiteral(self) -> bool: ...
    def numberLiteral(self) -> typing.Tuple: ...
    def stringLiteral(self) -> str: ...


class QQmlTypesExtensionInterface(Shiboken.Object):

    def __init__(self) -> None: ...

    def registerTypes(self, uri:bytes) -> None: ...


class QtQml(Shiboken.Object):
    @staticmethod
    def qmlAttachedPropertiesObject(arg__2:PySide2.QtCore.QObject, arg__3:PySide2.QtCore.QMetaObject, create:bool) -> typing.Tuple: ...
    @staticmethod
    def qmlAttachedPropertiesObjectById(arg__1:int, arg__2:PySide2.QtCore.QObject, create:bool=...) -> PySide2.QtCore.QObject: ...
    @staticmethod
    def qmlContext(arg__1:PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlContext: ...
    @staticmethod
    def qmlEngine(arg__1:PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlEngine: ...
    @staticmethod
    def qmlExecuteDeferred(arg__1:PySide2.QtCore.QObject) -> None: ...


class VolatileBool(object):
    @staticmethod
    def get() -> bool: ...
    @staticmethod
    def set(a:object) -> None: ...
@staticmethod
def qmlRegisterType(arg__1:type, arg__2:bytes, arg__3:int, arg__4:int, arg__5:bytes) -> int: ...

# eof
