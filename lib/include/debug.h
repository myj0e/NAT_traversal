//
//@Copyright:Copyright 2022 HOWV
//@License:
//@Birth:created by Howv on 2022-03-29
//@Content:log information console
//@Version:1.0.0
//@Revision:last revised by Howv on 2022-03-29
//



/*****************************************************************************************************/
/*                                                 INCLUDE                                           */
/*****************************************************************************************************/

#include <stdio.h>



/*****************************************************************************************************/
/*                                                 DEFINE                                            */
/*****************************************************************************************************/

#define DEBUG_OFF					0X00000000
#define DEBUG_DEBUG					0X00000001
#define DEBUG_INFO					0x00000010
#define DEBUG_ERROR					0x00000100


#define DEBUG_DEBUG(fmt, args...)			if(debug_level& DEBUG_DEBUG){printf("[%s:%d][DEBUG]"fmt"\n",__FILE__, __LINE__, args);}
#define DEBUG_INFO(fmt, args...)			if(debug_level& DEBUG_INFO){printf("[%s:%d][INFO]"fmt"\n",__FILE__, __LINE__, args);}
#define DEBUG_ERROR(fmt, args...)			if(debug_level& DEBUG_ERROR){printf("[%s:%d][ERROR]"fmt"\n",__FILE__, __LINE__, args);}


#define ERR_CHECK_GOTO(rv, tag) \
	if(ERR_NO_ERROR != (rv)) \
	{ \
		DEBUG_DEBUG("%s(%d) is error",#rv, rv); \
		goto tag; \
	}

#define COM_CHECK_GOTO(judge, tag) \
	if((judge)) \
	{ \
		DEBUG_DEBUG("%s is ture",#judge); \
		goto tag; \
	}

#define NULL_CHECK_GOTO(rv, tag) \
	if(NULL == (rv)) \
	{ \
		DEBUG_DEBUG("%s is NULL",#rv); \
		goto tag; \
	}

/*****************************************************************************************************/
/*                                                   TYPE                                            */
/*****************************************************************************************************/


/*****************************************************************************************************/
/*                                                 VARIABLE                                          */
/*****************************************************************************************************/

extern unsigned int debug_level;

/*****************************************************************************************************/
/*                                                 FUNCTION                                          */
/*****************************************************************************************************/

