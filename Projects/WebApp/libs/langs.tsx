export const output = (code:string = 'null') => {
  const lang = 'cn'

  type LanguageMessages = {
    [key: string]: string | { [key: string]: string };
  };

  const messages: LanguageMessages = {
    'cn': {
      'network_error': '网络连接发生问题,请稍后重试!',
      'uname_pwd_err': '用户名或密码错误!',
      'sign_in': '进入系统',
      'site_title': 'IPTV管理系统',
      'user_name': '用户名',
      'user_pwd': '密码',
      'user_name_empty': '用户名不能为空!',
      'user_pwd_empty': '密码不能为空!',
      'login_success': '登录成功!页面跳转中...',
      'menu_channel_list': '资源列表',
    },
  }

  if (typeof messages[lang] === 'object' && messages[lang].hasOwnProperty(code)) {
    return (messages[lang] as { [key: string]: string })[code];
  } else {
    return 'An unknown error occurred!!!'
  }
}
