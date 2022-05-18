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
PySide2.QtWinExtras, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWinExtras
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtWinExtras


class QWinColorizationChangeEvent(PySide2.QtWinExtras.QWinEvent):

    def __init__(self, color:int, opaque:bool) -> None: ...

    def color(self) -> int: ...
    def opaqueBlend(self) -> bool: ...


class QWinCompositionChangeEvent(PySide2.QtWinExtras.QWinEvent):

    def __init__(self, enabled:bool) -> None: ...

    def isCompositionEnabled(self) -> bool: ...


class QWinEvent(PySide2.QtCore.QEvent):

    def __init__(self, type:int) -> None: ...


class QWinJumpList(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    @typing.overload
    def addCategory(self, category:PySide2.QtWinExtras.QWinJumpListCategory) -> None: ...
    @typing.overload
    def addCategory(self, title:str, items:typing.Sequence=...) -> PySide2.QtWinExtras.QWinJumpListCategory: ...
    def categories(self) -> typing.List: ...
    def clear(self) -> None: ...
    def frequent(self) -> PySide2.QtWinExtras.QWinJumpListCategory: ...
    def identifier(self) -> str: ...
    def recent(self) -> PySide2.QtWinExtras.QWinJumpListCategory: ...
    def setIdentifier(self, identifier:str) -> None: ...
    def tasks(self) -> PySide2.QtWinExtras.QWinJumpListCategory: ...


class QWinJumpListCategory(Shiboken.Object):
    Custom                   : QWinJumpListCategory = ... # 0x0
    Recent                   : QWinJumpListCategory = ... # 0x1
    Frequent                 : QWinJumpListCategory = ... # 0x2
    Tasks                    : QWinJumpListCategory = ... # 0x3

    class Type(object):
        Custom                   : QWinJumpListCategory.Type = ... # 0x0
        Recent                   : QWinJumpListCategory.Type = ... # 0x1
        Frequent                 : QWinJumpListCategory.Type = ... # 0x2
        Tasks                    : QWinJumpListCategory.Type = ... # 0x3

    def __init__(self, title:str=...) -> None: ...

    def addDestination(self, filePath:str) -> PySide2.QtWinExtras.QWinJumpListItem: ...
    def addItem(self, item:PySide2.QtWinExtras.QWinJumpListItem) -> None: ...
    @typing.overload
    def addLink(self, icon:PySide2.QtGui.QIcon, title:str, executablePath:str, arguments:typing.Sequence=...) -> PySide2.QtWinExtras.QWinJumpListItem: ...
    @typing.overload
    def addLink(self, title:str, executablePath:str, arguments:typing.Sequence=...) -> PySide2.QtWinExtras.QWinJumpListItem: ...
    def addSeparator(self) -> PySide2.QtWinExtras.QWinJumpListItem: ...
    def clear(self) -> None: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def items(self) -> typing.List: ...
    def setTitle(self, title:str) -> None: ...
    def setVisible(self, visible:bool) -> None: ...
    def title(self) -> str: ...
    def type(self) -> PySide2.QtWinExtras.QWinJumpListCategory.Type: ...


class QWinJumpListItem(Shiboken.Object):
    Destination              : QWinJumpListItem = ... # 0x0
    Link                     : QWinJumpListItem = ... # 0x1
    Separator                : QWinJumpListItem = ... # 0x2

    class Type(object):
        Destination              : QWinJumpListItem.Type = ... # 0x0
        Link                     : QWinJumpListItem.Type = ... # 0x1
        Separator                : QWinJumpListItem.Type = ... # 0x2

    def __init__(self, type:PySide2.QtWinExtras.QWinJumpListItem.Type) -> None: ...

    def arguments(self) -> typing.List: ...
    def description(self) -> str: ...
    def filePath(self) -> str: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def setArguments(self, arguments:typing.Sequence) -> None: ...
    def setDescription(self, description:str) -> None: ...
    def setFilePath(self, filePath:str) -> None: ...
    def setIcon(self, icon:PySide2.QtGui.QIcon) -> None: ...
    def setTitle(self, title:str) -> None: ...
    def setType(self, type:PySide2.QtWinExtras.QWinJumpListItem.Type) -> None: ...
    def setWorkingDirectory(self, workingDirectory:str) -> None: ...
    def title(self) -> str: ...
    def type(self) -> PySide2.QtWinExtras.QWinJumpListItem.Type: ...
    def workingDirectory(self) -> str: ...


class QWinTaskbarButton(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def clearOverlayIcon(self) -> None: ...
    def eventFilter(self, arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtCore.QEvent) -> bool: ...
    def overlayAccessibleDescription(self) -> str: ...
    def overlayIcon(self) -> PySide2.QtGui.QIcon: ...
    def progress(self) -> PySide2.QtWinExtras.QWinTaskbarProgress: ...
    def setOverlayAccessibleDescription(self, description:str) -> None: ...
    def setOverlayIcon(self, icon:PySide2.QtGui.QIcon) -> None: ...
    def setWindow(self, window:PySide2.QtGui.QWindow) -> None: ...
    def window(self) -> PySide2.QtGui.QWindow: ...


class QWinTaskbarProgress(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def hide(self) -> None: ...
    def isPaused(self) -> bool: ...
    def isStopped(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def maximum(self) -> int: ...
    def minimum(self) -> int: ...
    def pause(self) -> None: ...
    def reset(self) -> None: ...
    def resume(self) -> None: ...
    def setMaximum(self, maximum:int) -> None: ...
    def setMinimum(self, minimum:int) -> None: ...
    def setPaused(self, paused:bool) -> None: ...
    def setRange(self, minimum:int, maximum:int) -> None: ...
    def setValue(self, value:int) -> None: ...
    def setVisible(self, visible:bool) -> None: ...
    def show(self) -> None: ...
    def stop(self) -> None: ...
    def value(self) -> int: ...


class QWinThumbnailToolBar(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def addButton(self, button:PySide2.QtWinExtras.QWinThumbnailToolButton) -> None: ...
    def buttons(self) -> typing.List: ...
    def clear(self) -> None: ...
    def count(self) -> int: ...
    def iconicLivePreviewPixmap(self) -> PySide2.QtGui.QPixmap: ...
    def iconicPixmapNotificationsEnabled(self) -> bool: ...
    def iconicThumbnailPixmap(self) -> PySide2.QtGui.QPixmap: ...
    def removeButton(self, button:PySide2.QtWinExtras.QWinThumbnailToolButton) -> None: ...
    def setButtons(self, buttons:typing.Sequence) -> None: ...
    def setIconicLivePreviewPixmap(self, arg__1:PySide2.QtGui.QPixmap) -> None: ...
    def setIconicPixmapNotificationsEnabled(self, enabled:bool) -> None: ...
    def setIconicThumbnailPixmap(self, arg__1:PySide2.QtGui.QPixmap) -> None: ...
    def setWindow(self, window:PySide2.QtGui.QWindow) -> None: ...
    def window(self) -> PySide2.QtGui.QWindow: ...


class QWinThumbnailToolButton(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def click(self) -> None: ...
    def dismissOnClick(self) -> bool: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def isEnabled(self) -> bool: ...
    def isFlat(self) -> bool: ...
    def isInteractive(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def setDismissOnClick(self, dismiss:bool) -> None: ...
    def setEnabled(self, enabled:bool) -> None: ...
    def setFlat(self, flat:bool) -> None: ...
    def setIcon(self, icon:PySide2.QtGui.QIcon) -> None: ...
    def setInteractive(self, interactive:bool) -> None: ...
    def setToolTip(self, toolTip:str) -> None: ...
    def setVisible(self, visible:bool) -> None: ...
    def toolTip(self) -> str: ...


class QtWin(Shiboken.Object):
    FlipDefault              : QtWin = ... # 0x0
    HBitmapNoAlpha           : QtWin = ... # 0x0
    FlipExcludeBelow         : QtWin = ... # 0x1
    HBitmapPremultipliedAlpha: QtWin = ... # 0x1
    FlipExcludeAbove         : QtWin = ... # 0x2
    HBitmapAlpha             : QtWin = ... # 0x2

    class HBitmapFormat(object):
        HBitmapNoAlpha           : QtWin.HBitmapFormat = ... # 0x0
        HBitmapPremultipliedAlpha: QtWin.HBitmapFormat = ... # 0x1
        HBitmapAlpha             : QtWin.HBitmapFormat = ... # 0x2

    class WindowFlip3DPolicy(object):
        FlipDefault              : QtWin.WindowFlip3DPolicy = ... # 0x0
        FlipExcludeBelow         : QtWin.WindowFlip3DPolicy = ... # 0x1
        FlipExcludeAbove         : QtWin.WindowFlip3DPolicy = ... # 0x2
    @staticmethod
    def colorizationColor() -> typing.Tuple: ...
    @typing.overload
    @staticmethod
    def disableBlurBehindWindow(window:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def disableBlurBehindWindow(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def enableBlurBehindWindow(window:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def enableBlurBehindWindow(window:PySide2.QtGui.QWindow, region:PySide2.QtGui.QRegion) -> None: ...
    @typing.overload
    @staticmethod
    def enableBlurBehindWindow(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def enableBlurBehindWindow(window:PySide2.QtWidgets.QWidget, region:PySide2.QtGui.QRegion) -> None: ...
    @staticmethod
    def errorStringFromHresult(hresult:int) -> str: ...
    @typing.overload
    @staticmethod
    def extendFrameIntoClientArea(window:PySide2.QtGui.QWindow, left:int, top:int, right:int, bottom:int) -> None: ...
    @typing.overload
    @staticmethod
    def extendFrameIntoClientArea(window:PySide2.QtGui.QWindow, margins:PySide2.QtCore.QMargins) -> None: ...
    @typing.overload
    @staticmethod
    def extendFrameIntoClientArea(window:PySide2.QtWidgets.QWidget, left:int, top:int, right:int, bottom:int) -> None: ...
    @typing.overload
    @staticmethod
    def extendFrameIntoClientArea(window:PySide2.QtWidgets.QWidget, margins:PySide2.QtCore.QMargins) -> None: ...
    @staticmethod
    def isCompositionEnabled() -> bool: ...
    @staticmethod
    def isCompositionOpaque() -> bool: ...
    @typing.overload
    @staticmethod
    def isWindowExcludedFromPeek(window:PySide2.QtGui.QWindow) -> bool: ...
    @typing.overload
    @staticmethod
    def isWindowExcludedFromPeek(window:PySide2.QtWidgets.QWidget) -> bool: ...
    @typing.overload
    @staticmethod
    def isWindowPeekDisallowed(window:PySide2.QtGui.QWindow) -> bool: ...
    @typing.overload
    @staticmethod
    def isWindowPeekDisallowed(window:PySide2.QtWidgets.QWidget) -> bool: ...
    @typing.overload
    @staticmethod
    def markFullscreenWindow(arg__1:PySide2.QtGui.QWindow, fullscreen:bool=...) -> None: ...
    @typing.overload
    @staticmethod
    def markFullscreenWindow(window:PySide2.QtWidgets.QWidget, fullscreen:bool=...) -> None: ...
    @staticmethod
    def realColorizationColor() -> PySide2.QtGui.QColor: ...
    @typing.overload
    @staticmethod
    def resetExtendedFrame(window:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def resetExtendedFrame(window:PySide2.QtWidgets.QWidget) -> None: ...
    @staticmethod
    def setCompositionEnabled(enabled:bool) -> None: ...
    @staticmethod
    def setCurrentProcessExplicitAppUserModelID(id:str) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowDisallowPeek(window:PySide2.QtGui.QWindow, disallow:bool) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowDisallowPeek(window:PySide2.QtWidgets.QWidget, disallow:bool) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowExcludedFromPeek(window:PySide2.QtGui.QWindow, exclude:bool) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowExcludedFromPeek(window:PySide2.QtWidgets.QWidget, exclude:bool) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowFlip3DPolicy(window:PySide2.QtGui.QWindow, policy:PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy) -> None: ...
    @typing.overload
    @staticmethod
    def setWindowFlip3DPolicy(window:PySide2.QtWidgets.QWidget, policy:PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy) -> None: ...
    @staticmethod
    def stringFromHresult(hresult:int) -> str: ...
    @typing.overload
    @staticmethod
    def taskbarActivateTab(arg__1:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarActivateTab(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarActivateTabAlt(arg__1:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarActivateTabAlt(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarAddTab(arg__1:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarAddTab(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarDeleteTab(arg__1:PySide2.QtGui.QWindow) -> None: ...
    @typing.overload
    @staticmethod
    def taskbarDeleteTab(window:PySide2.QtWidgets.QWidget) -> None: ...
    @typing.overload
    @staticmethod
    def windowFlip3DPolicy(arg__1:PySide2.QtGui.QWindow) -> PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy: ...
    @typing.overload
    @staticmethod
    def windowFlip3DPolicy(window:PySide2.QtWidgets.QWidget) -> PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy: ...

# eof
