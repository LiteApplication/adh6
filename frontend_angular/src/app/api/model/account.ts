/**
 * Adherent
 * Adherent api
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import { Member } from './member';

export interface Account { 
    /**
     * Account state
     */
    actif: boolean;
    /**
     * whether this account should be displayed first
     */
    pinned?: boolean;
    /**
     * ID of the account
     */
    id?: number;
    /**
     * Name of the account
     */
    name: string;
    /**
     * The type of account
     */
    type: number;
    /**
     * The date the account was created
     */
    creationDate?: Date;
    adherent?: Member;
}