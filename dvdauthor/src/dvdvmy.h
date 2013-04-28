/* A Bison parser, made by GNU Bison 2.5.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2011 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     NUM_TOK = 258,
     G_TOK = 259,
     S_TOK = 260,
     ID_TOK = 261,
     ANGLE_TOK = 262,
     AUDIO_TOK = 263,
     BREAK_TOK = 264,
     BUTTON_TOK = 265,
     CALL_TOK = 266,
     CELL_TOK = 267,
     CHAPTER_TOK = 268,
     CLOSEBRACE_TOK = 269,
     CLOSEPAREN_TOK = 270,
     COUNTER_TOK = 271,
     ELSE_TOK = 272,
     ENTRY_TOK = 273,
     EXIT_TOK = 274,
     FPC_TOK = 275,
     GOTO_TOK = 276,
     IF_TOK = 277,
     JUMP_TOK = 278,
     MENU_TOK = 279,
     NEXT_TOK = 280,
     OPENBRACE_TOK = 281,
     OPENPAREN_TOK = 282,
     PGC_TOK = 283,
     PREV_TOK = 284,
     PROGRAM_TOK = 285,
     PTT_TOK = 286,
     REGION_TOK = 287,
     RESUME_TOK = 288,
     RND_TOK = 289,
     ROOT_TOK = 290,
     SET_TOK = 291,
     SUBTITLE_TOK = 292,
     TAIL_TOK = 293,
     TITLE_TOK = 294,
     TITLESET_TOK = 295,
     TOP_TOK = 296,
     UP_TOK = 297,
     VMGM_TOK = 298,
     BOR_TOK = 299,
     LOR_TOK = 300,
     XOR_TOK = 301,
     _OR_TOK = 302,
     BAND_TOK = 303,
     LAND_TOK = 304,
     _AND_TOK = 305,
     NOT_TOK = 306,
     NE_TOK = 307,
     EQ_TOK = 308,
     LT_TOK = 309,
     LE_TOK = 310,
     GT_TOK = 311,
     GE_TOK = 312,
     SUB_TOK = 313,
     ADD_TOK = 314,
     MOD_TOK = 315,
     DIV_TOK = 316,
     MUL_TOK = 317,
     ADDSET_TOK = 318,
     SUBSET_TOK = 319,
     MULSET_TOK = 320,
     DIVSET_TOK = 321,
     MODSET_TOK = 322,
     ANDSET_TOK = 323,
     ORSET_TOK = 324,
     XORSET_TOK = 325,
     SEMICOLON_TOK = 326,
     COLON_TOK = 327,
     ERROR_TOK = 328
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 2068 of yacc.c  */
#line 91 "dvdvmy.y"

    unsigned int int_val;
    char *str_val;
    struct vm_statement *statement;



/* Line 2068 of yacc.c  */
#line 131 "dvdvmy.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE dvdvmlval;


